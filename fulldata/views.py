from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')

def myCv(request):
    return render(request, 'myCv.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    return render(request, 'contact.html')

