from django.forms import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        min_lenght=2,
        widget=forms.TextInput(
            attrs={'placeholder': 'Your name'}
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'E-mail'}
        )
    )
    message = forms.Charfield(
        min_length=20,
        widget=forms.Textarea(
            attrs={'placeholder': 'Message', 'cols': 30, 'rows': 9}
        )
    )