from django.contrib.auth.models import User
from django.core.checks import messages
from django.shortcuts import render
from . models import  department


# Create your views here.

def demo(request):
    obj=department.objects.all()
    return render(request,'index.html',{'result':obj,})



