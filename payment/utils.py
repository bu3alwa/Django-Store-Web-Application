from .models import Transactions, KnetTransactions, GotapTransactions
from payment.gotap import gotap
from payment.knet import knet
from django.conf import settings
import json

#def CreatePayment(ammount, returnurl, posturl, ordernumber, description, phonenumber, email, currency):
def GotapHandler(user, sub, payment_options):
    ammount = sub.price

    transaction = Transactions.objects.create(user=user, subscription=sub)

    trackid = transaction.trackid
    returnurl = 'https://bdoonlag.com/payment/gotap'
    email = user.email
    description = sub.name + " payment subscription"
    phonenumber = user.Profile.phone_number
    ordernumber = trackid
    currency = "KWD"

    response = gotap.CreatePayment(ammount, returnurl,  ordernumber, description, phonenumber, email, currency)

    if response == None:
        return None

    charge_id = response['id']

    paid = response['paid']

    gotaptrans = GotapTransactions.objects.create(
            charge_id=charge_id, 
            ammount=ammount, 
            currency=currency, 
            description=description, 
            paid=paid, 
            response=response)

    Transactions.objects.filter(pk=transaction.pk).update(GotapTransactions=gotaptrans)

    return response['redirect']['url']

def GotapUpdate(gotaptrans, url):
    response = gotap.RetrievePayment(gotaptrans.charge_id)

    if response == None:
        raise Http404("Response error please contact support")
    else:
        paid = response['paid']
        GotapTransactions.objects.filter(pk=gotaptrans.pk).update(response=response, paid=paid, urlresponse=url)

#CreatePayment(ammount, currencycode, retrunurl, errorurl, trackid):
def KnetHandler(user, sub, payment_options):
    ammount = sub.price

    transaction = Transactions.objects.create(user=user, subscription=sub)

    trackid = transaction.trackid
    returnurl = 'https://bdoonlag.com/payment/knet'
    email = user.email
    description = sub.name + " payment subscription"
    phonenumber = user.Profile.phone_number
    ordernumber = trackid
    currency = "414"

    response = knet.CreatePayment(ammount, currency, returnurl, returnurl, trackid)

    if response == None:
        return None

    paymentid = response.split(':')[0]
    path = ':'.join(response.split(':')[1:])

    redirecturl = knet.CreateURL(path, paymentid)

    knettrans = KnetTransactions.objects.create(
            ammount=ammount, 
            currencycode=currency, 
            paymentid=paymentid,
            )

    Transactions.objects.filter(pk=transaction.pk).update(KnetTransactions=knettrans)

    return redirecturl

#def RedirectPayment(RedirectURL, paymentID):
def KnetUpdate(knettrans, result, auth, ref, transid, postdate, url):
    if result == 'CAPTURED':
        paid = True
    else:
        paid = False

    KnetTransactions.objects.filter(pk=knettrans.pk).update(paid=paid, result=result, auth=auth, ref=ref, transid=transid)

    
    return "REDIRECT=https://" + settings.BASE_SITE_URL + '/?paymentID='  + knettrans.paymentid


