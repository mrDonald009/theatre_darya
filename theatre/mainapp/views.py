from django.shortcuts import redirect, render

# функции = вьюхи = контроллеры
def index(request):
    return render(request, 'mainapp/index.html')

def gallery(request):
    return render(request, 'mainapp/gallery.html')

def about_us(request):
    return render(request, 'mainapp/about_us.html')

def contacts(request):
    return render(request, 'mainapp/contacts.html')
