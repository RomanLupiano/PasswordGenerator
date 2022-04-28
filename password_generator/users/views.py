from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import PasswordForm
from .models import PasswordModel

@login_required
def user_home(request):
    passwords = PasswordModel.objects.filter(user=request.user)

    return render(request, 'userhome.html', {'passwords': passwords})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'register/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('index')
                #return render(request, 'authenticate/login.html', {'message': 'Error'})

    form = AuthenticationForm()
    
    return render(request, 'authenticate/login.html', {'form': form})

def CreatePassword(request):
    if request.method == 'POST':
        form = PasswordForm(request.POST)

        if form.is_valid():
            info = form.cleaned_data

            pwd = PasswordModel(user=request.user, platform=info['platform'], password=info['password'])

            pwd.save()

            return redirect('home')
    else:
        form = PasswordForm()

    return render(request, 'user_home/passwordcreate.html', {'form': form})

# class PasswordCreate(CreateView):
#     model = PasswordModel
#     success_url = 'users/user_home'
#     fields = ['platform', 'password'] 

# class PasswordUpdate(UpdateView):
#     model = PasswordModel
#     success_url = 'users/user_home'
#     fields = ['platform', 'password'] 

# class PasswordDelete(DeleteView):
#     model = PasswordModel
#     success_url = 'users/user_home'