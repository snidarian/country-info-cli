#!/usr/bin/python3


import requests as rq
import random as r
from colorama import Fore, Style


green = Fore.GREEN
blue = Fore.BLUE
yellow = Fore.YELLOW
reset = Fore.RESET



result = rq.get('https://restcountries.eu/rest/v2/all')


json_payload_list = result.json()

index = 0
for country_item in json_payload_list:
    print(str(index) + '. ' + country_item['name'] + ' - ' + country_item['alpha3Code'])
    index+=1







