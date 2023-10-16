from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(reguest):
    if reguest.method =='POST':
        username=reguest.POST['username']
        password=reguest.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(reguest,user)
            return redirect('add')
        else:
            messages.info(reguest,"invalid register")
            return redirect('login')
    return render(reguest,'login.html')

def register(request, user=None):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Token")
                return redirect(register)

            elif User.objects.filter(email=email).exists():
                messages.info(request, "email Taken")
                return redirect(register)
            else:

                user = User.objects.create_user(username=username, password=password,email=email)
                user.save();
                return redirect('login')
        else:
            messages.info(request, "password is not correct")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')

def form(request):
    if request.method == 'POST':
        username = request.POST['name']

        if User.objects.filter(username=username):
            messages.info(request, "Order Confirmed ")
        return render(request, 'form.html')

    return render(request,'form.html')




def logout(request):
    auth.logout(request)
    return redirect('/')

