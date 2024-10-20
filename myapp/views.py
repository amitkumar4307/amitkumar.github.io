from django.shortcuts import render, redirect
from .models import AdminLogin
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def services(request):
    return render(request,'services.html')
def service_details(request):
    return render(request, 'service-details.html')
def resume(request):
    return render(request, 'resume.html')
def Dashboard(request):
    return render(request, 'Dashboard.html')
def logcode(req):
    if req.method=="POST":
        adminType=req.POST['adminType']
        user=req.POST['user']
        password=req.POST['password']
        if adminType=='admin':
            try:
                user=AdminLogin.objects.get(user=user,password=password)
                if user is not None:
                    req.session['adminid']=user.user
                    return redirect('myapp:Dashboard')
            except ObjectDoesNotExist:
                return render(req,'Dashboard.html',{'msg':'Invalid user'})