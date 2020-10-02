from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate,login, logout

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request,'index.html')
    else:
        return redirect("/login")
    return render(request,'index.html')


def loginUser(request):
    
    if request.method =="POST":
        #check if user has entered correct credentials
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(username=username, password=password)
        if user is not None:
        # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
        else:
    # No backend authenticated the credentials
            messages.info('Invalid credentials')
            return render(request,'login.html')
    return render(request,'login.html')


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username): 
                messages.info(request,'Username already taken!')
                return redirect('register')
            elif User.objects.filter(email=email):
                messages.info(request,'Email already taken!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save();
                messages.info(request,'User Created Successfully!')
                return redirect('login')
        else:
            messages.info(request,'Your password doesnot match!')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')