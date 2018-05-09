from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from .forms import ProfileForm, BillingForm
from django.contrib import messages
from .models import Profile, Subscription
from store.models import SubscriptionModel
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.http import require_http_methods
from payment.utils import GotapHandler, KnetHandler

def profile_required(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        try:
            profile = request.user.Profile
        except ObjectDoesNotExist:
            profile = None

        if profile == None:
            messages.info(request, "Must have a profile")
            return redirect('/account/profile')
        else:
            return function(request, *args, **kwargs)
    return wrap

@login_required
def index(request):
    user = request.user
    try:
        sub = request.user.Subscription
    except ObjectDoesNotExist:
        sub = None


    if request.method == "POST":
        if sub != None:
            messages.success(request, "Free Trial has expired")
            return redirect('/account')

        else:
            today = date.today()
            submodel = SubscriptionModel.objects.filter(name='Free Trial').first()
            end_date = today + timedelta(days=int(submodel.length))
            s = Subscription.objects.create(
                    user=user,
                    renew=False,
                    subscription=submodel,
                    start_date=date.today(),
                    end_date=end_date,
                    )

            return redirect('/account')

    else:
        if sub != None:
            subscription = sub.order_by('-end_date').first()

            return render(request, 'account/index.html', {'user': user, 'account': subscription })

        return render(request, 'account/index.html', {'user': user })

@login_required
def profile(request):
    user = request.user

    try:
        profile = request.user.Profile
    except ObjectDoesNotExist:
        profile = None


    if request.method == "POST":
        if profile != None:
            f = ProfileForm(data=request.POST, instance=profile)
        else:
            f = ProfileForm(data=request.POST)

        f.instance.user = user

        if f.is_valid():
            f.clean()
            f.save()
            messages.success(request, "Your profile has been updated")
            return redirect("/account/profile") 

    else:
        if profile != None:
            f = ProfileForm(instance=profile)
        else:
            f = ProfileForm()

    return render(request, 'account/profile.html', {'form': f})

@login_required
@profile_required
def billing(request):
    if request.method == "POST":
        form = BillingForm(request.POST)
        if form.is_valid(): 
            sub_selected = form.cleaned_data['subscription_type']
            sub = SubscriptionModel.objects.get(id=sub_selected)
            payment_options = form.cleaned_data['payment_options']
            user = request.user

            if payment_options == "KNET":
                redirect_url = KnetHandler(user, sub, payment_options)
            elif payment_options == "GoTap":
                redirect_url = GotapHandler(user, sub, payment_options)
            if redirect_url != None:
                return redirect(redirect_url)
            else:
                messages.Error(request, "Payment gateway failure, please try again later")
                return redirect('/account/billing')
                

    else:
        f = BillingForm()
        return render(request, 'account/billing.html', {'form': f})

@login_required
@require_http_methods(["POST"])
def cancel(request):
    pass

