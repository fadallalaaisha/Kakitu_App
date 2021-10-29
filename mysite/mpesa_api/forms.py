from django import forms

class CutomerForm(forms.Form):
    phone = forms.CharField(max_length=20, required=True,)
    amount = forms.IntegerField(min_value=2, required=True)

  