import requests
import datetime
from pprint import pprint as pp
import json


def symbols():
    with open('symbols.json', 'r') as file:
        symbols_file = json.load(file)
    return symbols_file


def values():
    currency_from = input("Please enter your currency or USD by default: ")
    if currency_from == '' or currency_from not in symbols_file['symbols']:
        currency_from = 'USD'
    currency_to = input("Please enter your currency or UAH by default: ")
    if currency_to == '' or currency_to not in symbols_file['symbols']:
        currency_to = 'UAH'
    return currency_from, currency_to


def convert():
    amount = 10000.5
    start_date = datetime.datetime.now() - datetime.timedelta(days=4)
    result = [['date', 'from', 'to', 'amount', 'rate', 'result']]
    while start_date <= datetime.datetime.now():
        request = requests.get('https://api.exchangerate.host/convert?',
                               params={'from': currency_from, 'to': currency_to, 'amount': amount, 'date': start_date})
        data = request.json()
        result.append([data['date'],
                       data['query']['from'],
                       data['query']['to'],
                       data['query']['amount'],
                       data['info']['rate'],
                       data['result']])
        start_date += datetime.timedelta(days=1)
    pp(result)

convert()



