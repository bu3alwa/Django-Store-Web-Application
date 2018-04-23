from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import SubscriptionModel

# Create your views here.


def index(request):
    return render(request, 'store/index.html')

def subscribe(request):
    submodel = SubscriptionModel.objects.all()
    submodel = submodel.exclude(length='14')
    return render(request, 'store/subscribe_page.html', { 'submodel': submodel })

def contact(request):
    return render(request, 'store/contact.html')

def terms(request):
    return render(request, 'store/terms.html')
