from django import forms
from .models import PropertyBook


class PropertyBookForm(forms.ModelForm):
    check_in = forms.DateField(widget=forms.DateInput(attrs={'id': 'checkin_date'}))
    check_out = forms.DateField(widget=forms.DateInput(attrs={'id': 'checkout_date'}))
    class Meta:
        model = PropertyBook
        fields = ['check_in', 'check_out', 'guest', 'children']
























