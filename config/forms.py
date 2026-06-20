from config.models import  Foydalanuvchi
from django import forms

class FoydalanuvchiForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parol yarating'})
    )

    class Meta:
        model = Foydalanuvchi
        fields = ['name', 'surname', 'age', 'email']
        widgets = {
            'name':    forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ismingizni kiritng'}),
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'familyangizni kiriting'}),
            'age':     forms.NumberInput(attrs={'class': 'form-control'}),
            'email':   forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Emailingizni kiritng'}),
        }

class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Parol'})
    )
    eslab_qol = forms.BooleanField(required=False, label='Meni eslab qol')