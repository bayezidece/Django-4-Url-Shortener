from django import forms

class UrlForm(forms.Form):
    link_url = forms.URLField(
        label=False, 
        max_length=5000, 
        widget=forms.URLInput(attrs={
            'size': '120', 
            'placeholder': 'Enter URL Here', 
            'autocomplete': 'off'
            })
        )