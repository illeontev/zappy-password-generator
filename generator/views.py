from django.shortcuts import render
from django.http import HttpResponse
import random
import string

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characters = string.ascii_lowercase

    if request.GET.get('uppercase'):
        characters += string.ascii_uppercase

    if request.GET.get('special'):
        characters += '#$@%^&*()'

    if request.GET.get('numbers'):
        characters += '0123456789'

    length = int(request.GET.get('length', 12))

    thepassword = ""
    for i in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')