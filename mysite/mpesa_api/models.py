from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class MpesaPayment(models.Model):
    phone_number = PhoneNumberField()
   