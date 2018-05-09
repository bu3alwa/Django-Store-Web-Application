from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from datetime import date, timedelta
from account.models import Subscription
from django.views import View
from .utils import *

class KnetProcess(View):
    def get(self, request, *args, **kwargs):
        paymentid = request.GET.get("PaymentID")
        trans_exists = Transactions.objects.filter(KnetTransactions__paymentid__contains=paymentid).exists()

        if not trans_exists:
            return HttpResponseNotFound("Does not exist")
        
        trans = Transactions.objects.select_related("user").filter(KnetTransactions__paymentid__contains=paymentid)

        if trans.user != request.user:
            return HttpResponse('Unauthorized', status=401)


        if trans.KnetTransactions.paid == True:
            messages.success(request, "Payment successful")
        else:
            messages.info(request, "Payment Failed")

        return redirect('/account/')

    def post(self,request, *args, **kwargs):
        paymentid = request.POST.get("paymentid")
        result = request.POST.get("result")
        auth = request.POST.get("auth")
        ref = request.POST.get("ref")
        transid = request.POST.get("tranid")
        postdate = request.POST.get("postdate")
        postdate = date(date.today().year, postdate[:1], postdate[2:3:])
        trackid = request.POST.get("trackid")

        trans_exists = Transactions.objects.filter(trackid=trackid).filter(KnetTransactions__paymentid__contains=paymentid).exists()

        if not trans_exists:
            return HttpResponseNotFound("Does not exist")

        trans = Transactions.objects.select_related("KnetTransactions").filter(trackid=trackid)

        if trans.subscription_update == True:
            return HttpReponseNotFound("Already updated")
        #KnetUpdate(knettrans, result, auth, ref, transid, postdate, url):
        KnetUpdate(trans.KnetTransactions, result, auth, ref, transid, postdate, request.path) 
        trans.refresh_from_db()

        if trans.KnetTransactions.paid:
            today = date.today()
            submodel = trans.subscription

            sub = Subscription.objects.filter(user=trans.user).order_by('-end_date').first()

            if sub.end_date > date.today():
                end_date = sub.end_date
            else:
                end_date = date.today()

            end_date =  end_date + timedelta(days=int(submodel.length) * 365/12)
            s = Subscription.objects.create(
                    user=trans.user,
                    renew=False,
                    subscription=submodel,
                    start_date=date.today(),
                    end_date=end_date,
                    )

        Transactions.objects.filter(pk=trans.pk).update(subscription_updated=True)


def gotap_process(request):
    charge_id = request.GET.get("chargeid")
    gotap_exists = GotapTransactions.objects.filter(charge_id=charge_id).exists()

    if not gotap_exists:
        return HttpResponseNotFound("Does not exist")

    gotaptrans = GotapTransactions.objects.filter(charge_id=charge_id).first()
    
    try:
        GotapUpdate(gotaptrans, request.path)
    except Http404:
        return HttpResponseNotFound("Payment gateway failure. Please contact support")

    gotaptrans.refresh_from_db()

    if gotaptrans.paid:
        today = date.today()
        trans = Transactions.objects.select_related('GotapTransactions').get(GotapTransactions=gotaptrans)
        submodel = trans.subscription

        sub = Subscription.objects.filter(user=trans.user).order_by('-end_date').first()

        if sub.end_date > date.today():
            end_date = sub.end_date
        else:
            end_date = date.today()

        end_date =  end_date + timedelta(days=int(submodel.length) * 365/12)
        s = Subscription.objects.create(
                user=trans.user,
                renew=False,
                subscription=submodel,
                start_date=date.today(),
                end_date=end_date,
                )

        Transactions.objects.select_related("GotapTransactions").filter(GotapTransactions=gotaptrans).update(subscription_updated=True)
        messages.success(request, "Payment successful")
    else:
        messages.info(request, "Payment Failed")

    return redirect('/account/')

    
