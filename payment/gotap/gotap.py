import requests
from .local_settings import *
import json


def CreatePayment(ammount, returnurl, ordernumber, description, phonenumber, email, currency):
    headers = {'Authorization': 'Bearer {}'.format(API_KEY_SECRET),
            'Content-Type': 'application/json'}

    data = {"amount": ammount,"currency": currency,"statement_descriptor": description,"redirect":{"return_url": returnurl},"description": description,"metadata":{"Order Number":ordernumber},"receipt_sms": phonenumber,"receipt_email":email}

    url = 'https://api.tap.company/v1/charges/'
    r = requests.post(url, headers=headers, data=json.dumps(data))
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        return None


def RetrievePayment(charge_id):
    headers = {'Authorization': 'Bearer {}'.format(API_KEY_SECRET),
            'Content-Type': 'application/json'}
    data = {}

    url = 'https://api.tap.company/v1/charges/' + charge_id
    r = requests.get(url, headers=headers, data=json.dumps(data))

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        return None


def UpdatePayment(charge_id, ammount, returnurl, ordernumber, description, phonenumber, email, currency):
    headers = {'Authorization': 'Bearer {}'.format(API_KEY_SECRET),
            'Content-Type': 'application/json'}

    data = {"amount": ammount,"currency": currency,"statement_descriptor": description,"redirect":{"return_url": returnurl},"description": description,"metadata":{"Order Number":ordernumber},"receipt_sms": phonenumber,"receipt_email":email}

    url = 'https://api.tap.company/v1/charges/' + charge_id
    r = requests.put(url, headers=headers, data=json.dumps(data))

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        return None


def CreateRefund(charge_id, ammount, reason, order_number):
    headers = {'Authorization': 'Bearer {}'.format(API_KEY_SECRET),
            'Content-Type': 'application/json'}

    data = {"charge": charge_id,
            "amount": ammount,
            "reason": reason,
            "metadata": {
            "Order Number": ordernumber
                } 
            }

    url = 'https://api.tap.company/v1/refunds/'
    r = requests.post(url, headers=headers, data=json.dumps(data))
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        return None



def GetRefund(refund_id):
    headers = {'Authorization': 'Bearer {}'.format(API_KEY_SECRET),
            'Content-Type': 'application/json'}


    data = {}
    url = 'https://api.tap.company/v1/refunds/' + refund_id
    r = requests.get(url, headers=headers, data=json.dumps(data))

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        return None


