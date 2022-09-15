from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm

# функции = вьюхи = контроллеры
def index(request):
    return render(request, 'mainapp/index.html')

def gallery(request):
    return render(request, 'mainapp/gallery.html')

def about_us(request):
    return render(request, 'mainapp/about_us.html')

def contacts(request):
    return render(request, 'mainapp/contacts.html')

def email_address(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'saveliy_petrov_2011@mail.ru', ['vogue_1990@mail.ru'], fail_silently=False)
            if mail:
                messages.success(request, 'Письмо отправлено!')
                return redirect('email_address')
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = ContactForm()
    return render(request, 'mainapp/email_address.html', {'form: form'})