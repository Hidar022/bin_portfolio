from django.shortcuts import render

def home(request):
    return render(request, "portfolio/index.html")

def techstack(request):
    return render(request, "portfolio/techstack.html")

def contact(request):
    return render(request, "portfolio/contact.html")
