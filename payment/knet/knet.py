import requests
from .local_settings import *


def CreatePayment(ammount, currencycode, returnurl, errorurl, trackid):
    headers = {'Content-Type': 'x-www-form-urlencoded'}

    data = {'id': KNET_ID, 'password': KNET_PASSWORD, 'action': '1', 'amt': ammount, 'currecycode': currencycode, 'responseURL': returnurl, 'errorURL': errorurl, 'trackid': trackid }

    url = KNET_URL
    r = requests.post(url, headers=headers, params=data)

    if r.status_code == requests.codes.ok:
        return r.text
    else:
        return None

def CreateURL(path, paymentid):
    return path + '/?PaymentID=' + paymentid

