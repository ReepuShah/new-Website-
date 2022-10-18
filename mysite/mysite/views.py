from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def product(request):
    return render(request,'product.html')

def three_wheelers(request):
    return render(request,'three-wheelers.html')

def overview(request):
    return render(request,'overview.html')

def technology(request):
    return render(request,'technology.html')

def dealernetwork(request):
    return render(request,'dealernetwork.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

