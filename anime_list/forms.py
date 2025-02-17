from django import forms

class SearchForm(forms.Form):
   query = forms.CharField(
        required=False,  
        label="",  
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '🔍 Введіть назву аніме...'})
    )