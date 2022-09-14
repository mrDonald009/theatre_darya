from django.shortcuts import render

# функции = вьюхи = контроллеры
def index(request):
    return render(request, 'mainapp/index.html')

def gallery(request):
    return render(request, 'mainapp/gallery.html')

