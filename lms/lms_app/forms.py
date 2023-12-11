from django import forms
from .models import *


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields='__all__'
    widgets={'name' :forms.TextInput(attrs={'cLass':'form-control'})}
            
class BookForm(forms.ModelForm):
    class Meta:
        model =Book
        fields=['title',
                'auther',
                'photo_book',
                'photo_auther',
                'pages',
                'price',
                'rental_price_day',
                'rental_time',
                'total_price',
                'status',
                'category']
    widgets ={
        'title': forms.TextInput(attrs={'class' : 'form-control'}),
        'auther': forms.TextInput(attrs={'class':'form-control'}),
        'photo_book': forms.FileInput(attrs={'class':'form-control'}),
        'photo_auther': forms.FileInput(attrs={'class':'form-control'}),
        'pages': forms.NumberInput(attrs={'class':'form-control'}),
        'price': forms.NumberInput(attrs={'class':'form-control'}),
        'rental_price_day': forms.NumberInput(attrs={'class':'form-control' , 'id':'rental_price'}),
        'rental_time': forms.NumberInput(attrs={'class':'form-control', 'id':'rental_time'}),
        'total_price': forms.NumberInput(attrs={'class':'form-control', 'id':'total'}),
        'status': forms.Select(attrs={'class':'form-control'}),
        'category': forms.Select(attrs={'class':'form-control'}),
    }