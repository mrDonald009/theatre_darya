from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    #email = forms.EmailInput(label='email', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))