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

#args = parser.add_argument('--all', '-a', help="Shows all countries and their calling codes")
args = parser.add_argument('fullname', help="Shows all countries and their calling codes", type=str, nargs='*')

args = parser.parse_args()


# makes request to webAPI for country information
result = rq.get('https://restcountries.eu/rest/v2/all')


json_payload_list = result.json()


for arg in args.fullname:
    result = rq.get(f'https://restcountries.eu/rest/v2/name/{arg}?fullText=true')
    json_payload = result.json()
    json_payload = json_payload[0]
    print(json_payload)







