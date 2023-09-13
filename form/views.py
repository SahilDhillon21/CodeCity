from django.shortcuts import render, redirect
from form.models import Donator
from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
import smtplib
from email.message import EmailMessage

from django.core.mail import send_mail

def formInput(request):
    return render(request,"form/formInput.html")

def addData(request):
    if request.method == 'POST':
        donation_type = request.POST['donation_type']
        amount = request.POST['amount']
        fname = request.POST['first']
        lname = request.POST['last']
        address = request.POST['address']
        email = request.POST['email']
        phone = request.POST['phone']
        city = request.POST['city']
        state = request.POST['state']
        state = request.POST['country']
        
        print(donation_type)

        donator = Donator.objects.create(
            donation_type = donation_type,
            amount = amount,
            address = address,
            city = city,
            fname = fname,
            lname = lname,
            state = state,
            email = email,
            mobile = phone,
        )
        donator.save()

        # msg = EmailMessage()

        # msg['Subject'] = 'Thank you for your donation!'
        # msg['From'] = '658sahil@gmail.com'
        # msg['To'] = email
        # msg.set_content("Thank you for donating "+str(amount)+", "+fname+" "+lname+"!")
        
        # s = smtplib.SMTP('127.0.0.1',8000)
        # s.send_message(msg)
        # s.quit()

        send_mail(
        "Thank you for your donation!",
        "Thank you "+fname+" "+lname+" for donating "+amount+"!",
        "658sahil@gmail.com",
        [str(email)],
        fail_silently=False,
        )

        return redirect(formInput)
    
def displayData(request):
    donators = Donator.objects.all()
    context = {'donators':donators}
    return render(request,'form/displayData.html',context)



def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

#Opens up page as PDF
class ViewPDF(View):
	def get(self, request, name, *args, **kwargs):
            donator_invoice = Donator.objects.get(fname=name)
            
            data = {}
            data["fname"] = donator_invoice.fname
            data["lname"] = donator_invoice.lname
            data["address"] = donator_invoice.address
            data["amount"] = donator_invoice.amount
            data["city"] = donator_invoice.city
            data["email"] = donator_invoice.email
            data["mobile"] = donator_invoice.mobile
            data["state"] = donator_invoice.state
            
            pdf = render_to_pdf('form/pdf_template.html', data)
            return HttpResponse(pdf, content_type='application/pdf')


#Automaticly downloads to PDF file
class DownloadPDF(View):
	def get(self, request, name, *args, **kwargs):
		
            donator_invoice = Donator.objects.get(fname=name)
                
            data = {}
            data["fname"] = donator_invoice.fname
            data["lname"] = donator_invoice.lname
            data["address"] = donator_invoice.address
            data["amount"] = donator_invoice.amount
            data["city"] = donator_invoice.city
            data["email"] = donator_invoice.email
            data["mobile"] = donator_invoice.mobile
            data["state"] = donator_invoice.state
            

            pdf = render_to_pdf('app/pdf_template.html', data)

            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response



def index(request):
	context = {}
	return render(request, 'app/index.html', context)

def chartData(request):
    donors = Donator.objects.all()
    donor_names = ""
    donor_amounts = ""
    donor_ages = ""
    donor_percent = ""
    total_amount = 0

    for d in donors:
        total_amount = total_amount + d.amount

    for d in donors:
          donor_names = donor_names + d.fname +" "
          donor_amounts = donor_amounts + str(d.amount)+" "
          donor_ages = donor_ages + str(d.age)+" "
          donor_percent = donor_percent + str((d.amount/total_amount)*100) + " "

    print(donor_percent)

    context = {
          'donors':donors, 
          'donor_names':donor_names,
          'donor_amounts':donor_amounts,
          'ages':donor_ages,
          'donor_percent':donor_percent,
          'total_amount':total_amount,
    }
    return render(request,'form/chart.html',context)