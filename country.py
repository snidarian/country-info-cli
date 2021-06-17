#!/usr/bin/python3


import requests as rq
import random as r
import argparse
from colorama import Fore, Style


green = Fore.GREEN
blue = Fore.BLUE
yellow = Fore.YELLOW
reset = Fore.RESET



# setup argparse
parser = argparse.ArgumentParser(description="Query country info")

args = parser.add_argument('--all', '-a', help="Shows all countries and their calling codes")
args = parser.add_argument('fullname', help="Shows all countries and their calling codes", type=str, nargs='?')

args = parser.parse_args()


# makes request to webAPI for country information
result = rq.get('https://restcountries.eu/rest/v2/all')


json_payload_list = result.json()



index = 0
for country_item in json_payload_list:
    print(str(index) + '. ' + country_item['name'] + ' - ' + country_item['callingCodes'][0])
    index+=1







