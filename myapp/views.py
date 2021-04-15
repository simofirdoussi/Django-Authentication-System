from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

def registrationView(response):

    if response.method=='POST':
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserCreationForm()
    return render(response, 'myapp/register.html', {'form' : form})


def loginView(request):
    username = request.POST.get('username',)
    password = request.POST.get('pass',)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
    return render(request, 'myapp/login.html')

def logoutpage(request):
    logout(request)
    return redirect('register')

def index(request):
    return render(request, 'myapp/index.html')