from django import forms
from .models import MpesaPayment

class CutomerForm(forms.ModelForm):
    # phone = forms.CharField(max_length=20, required=True, help_text='Phone number')

    class Meta:
        model=MpesaPayment
        fields="__all__"