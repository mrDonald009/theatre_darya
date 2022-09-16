from django.shortcuts import render
from django.forms import models
# функции = вьюхи = контроллеры


def index(request):
    return render(request, 'mainapp/index.html')

def gallery(request):
    return render(request, 'mainapp/gallery.html')

def about_us(request):
    return render(request, 'mainapp/about_us.html')

def contacts(request):
    return render(request, 'mainapp/contacts.html')

def create_email(request):
    return render(request, 'mainapp/create_email.html')


def test_context(request):
    context = {
        'title' : 'geekshop',
        'header' : 'Добро пожаловать на сайт!',
        'username' : 'Иван Иванов',
    }
    return render(request, 'mainapp/test-context.html', context)