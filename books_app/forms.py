from .models import Books,Category
from django import forms


class categoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'})
            }

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ('title', 'author','book_image', 'author_photo', 'prices', 'status', 'category', 'retail_price_day', 'retail_period', 'total_rental','pages')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'book_image':forms.FileInput(attrs={'class':'form-control'}),
            'author_photo':forms.FileInput(attrs={'class':'form-control'}),
            'prices':forms.NumberInput(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'retail_price_day':forms.NumberInput(attrs={'class':'form-control', 'id':'rentalprice'}),
            'retail_period':forms.NumberInput(attrs={'class':'form-control', 'id': 'rentaldays'}),
            'total_rental':forms.NumberInput(attrs={'class':'form-control', 'id':'totalrental'}),
            'pages':forms.NumberInput(attrs={'class':'form-control'}),
            
        }