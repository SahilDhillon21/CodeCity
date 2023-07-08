from django.shortcuts import render

def merchhome(request):
    return render(request,'merchandise/merchhome.html')

def cart(request):
    return render(request, 'merchandise/cart.html')

def checkout(request):
    return render(request, 'merchandise/checkout.html')

# Create your views here.
