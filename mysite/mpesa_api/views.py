from datetime import date
from django.http import HttpResponse
from django.shortcuts import render
from .forms import CutomerForm
from django.contrib.auth.decorators import login_required
import requests
from requests.auth import HTTPBasicAuth
import json
from . mpesa_credentials import MpesaAccessToken, LipanaMpesaPpassword
import logging
logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'index.html')
    
def getAccessToken(request):
    consumer_key = 'cHnkwYIgBbrxlgBoneczmIJFXVm0oHky'
    consumer_secret = '2nHEyWSD4VjpNh2g'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['']
    return HttpResponse(validated_mpesa_access_token)


def lipa_na_mpesa_online(request):
    form = CutomerForm(request.POST)

    if form.is_valid():
         phone = form.cleaned_data['phone']
    amount = form.cleaned_data['amount']

    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

    headers = {"Authorization": "Bearer %s" % access_token,"Content-Type":"application/json"}
    request = {
        "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
        "Password": LipanaMpesaPpassword.decode_password,
        "Timestamp": LipanaMpesaPpassword.lipa_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": int(phone),  
        "PartyB": LipanaMpesaPpassword.Business_short_code,
        "PhoneNumber": int(phone),  
        "CallBackURL": "https://aisha.com",
        "AccountReference": "Aisha",
        "TransactionDesc": "Testing"
    }
    logger.info('Phone number:' + phone)
    logger.info('Amount:' + str(amount))
    logger.info(request)

    response = requests.request('post',api_url, headers=headers, json=request)
    return HttpResponse(response)

    # return HttpResponse('Not working')
 
   
def register_Customer(request):
    return render(request,'customer.html',{'form': CutomerForm()})