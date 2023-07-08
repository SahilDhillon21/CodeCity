from django.shortcuts import render, redirect
from .models import Contact, Profile
from codepub.views import profile
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,'home/home.html')

def about(request):
    return render(request,'home/about.html')

def contact(request):
    if request.method=='POST':
        # The values are identified and retrived using the 'name="xyx"' attribute in the input field of the form.
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']


        if len(name)<2:
            messages.error(request,"Name is too short.")

        elif len(phone)<10:
            messages.error(request,"Phone number must be 10 digits!")


        elif len(content)<10:
            messages.error(request,"Message is too short.")


        else:
            contact = Contact(name = name, email = email, phone = phone, content = content)
            contact.save()
            messages.success(request,"Message sent successfuly!")


    return render(request,'home/contact.html')


def signup(request):
    if request.method == 'POST':
        citizenID = request.POST['citizenID']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if(password1==password2):
            if User.objects.filter(email=email).exists():
                messages.info(request,'This email already exists. Login instead?')
                return redirect(signup)
            if User.objects.filter(username=citizenID).exists():
                messages.warning(request,'Username already taken. Please try another.')
                return redirect(signup)
            else:
                newUser = User.objects.create_user(username=citizenID,email=email, password=password1)
                newUser.save()

                #Log user in and redirect to settings page

                user_login = auth.authenticate(username=citizenID,password = password1)
                auth.login(request,user_login)

                #create a profile for the new user
                user_model = User.objects.get(username=citizenID)
                new_profile = Profile.objects.create(user=user_model, citizenID=user_model.id)
                new_profile.save()

                messages.success(request,'Citizen registered successfully!')
                return redirect(profile)
        else:
            messages.info(request, 'Passwords do not match!')
            return redirect(signup)


    return render(request,'home/signup.html')

def login(request):
    if request.method == 'POST':
        citizenID = request.POST['citizenID']
        password = request.POST['password']

        user = auth.authenticate(username = citizenID, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect(index)
        else:
            messages.info(request,'Invalid credentials')
            return redirect(login)
    return render(request,'home/login.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request,'Logged out successfully')
    return redirect(index)