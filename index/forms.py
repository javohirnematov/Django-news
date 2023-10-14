from django import forms
from .models import Product
from django.forms import ModelForm, TextInput, Textarea, ImageField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SearchForm(forms.Form):
    search_product = forms.CharField(max_length=256)

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProductForm(ModelForm):
    product_photo = forms.ImageField()
    class Meta:
        model = Product

        fields = ['product_name', 'product_category', 'product_des', 'product_photo']

        widgets = {
            "product_name": TextInput(attrs={'class': 'form-control', 'placeholder': 'Название статьи'}),
            "product_category": TextInput(attrs={'class': 'form-control', 'placeholder': 'Анонс статьи'}),
            "product_des": Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст статьи'}),
            #"product_photo": ImageField(attrs={'class': 'form-control', 'placeholder': 'Фото статьи'}),
        }

