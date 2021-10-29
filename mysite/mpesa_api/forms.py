from django import forms

class CutomerForm(forms.Form):
    phone = forms.CharField(max_length=20, required=True,)
    amount = forms.IntegerField(min_value=5, required=True)

  