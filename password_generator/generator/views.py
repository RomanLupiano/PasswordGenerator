from django.shortcuts import render
from django.http import HttpResponse
from random import choice

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    generated_password = ''

    lenght = int(request.GET.get('lenght'))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('/*-+=!?@#$%&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    for i in range(lenght):
        generated_password += choice(characters)



    return render(request, 'password.html', {'password': generated_password})
