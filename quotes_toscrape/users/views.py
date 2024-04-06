from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from .forms import AuthorForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/users/add_author')
    else:
        form = RegistrationForm()

    return render(request, 'users/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/users/add_author')
    else:
        form = AuthenticationForm()
    
    return render(request, 'users/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('/')

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/users/add_author')
    else:
        form = AuthorForm()
    
    return render(request, 'users/add_author.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'users/login.html'

class CustomLogoutView(LogoutView):
    next_page = '/'

# Create your views here.
