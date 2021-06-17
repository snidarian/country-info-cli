#!/usr/bin/python3


import requests as rq
import random as r
import argparse
import json
from colorama import Fore, Style


red = Fore.RED
green = Fore.GREEN
blue = Fore.BLUE
yellow = Fore.YELLOW
cyan = Fore.CYAN
reset = Fore.RESET


# ------------------------------------------------------------------------------------------
# DEFINITIONS

def print_country_information(parent_dictionary) -> None:
    print("Country: " + green + parent_dictionary['name'] + reset)
    print("CallingCode:" + green + str(parent_dictionary['callingCodes']) + reset)
    print("Capital:" + green + parent_dictionary['capital'] + reset)
    print("Region:" + green + parent_dictionary['region'] + reset)
    print("Subregion:" + green + parent_dictionary['subregion'] + reset)
    # languages
    print("languages:", end=' ')
    for language in parent_dictionary['languages']:
        print(green + language['name'] + reset + ', ', end='')
    print("")
    # population
    print(f"Population:" + green + str(parent_dictionary['population']) + reset)
    print("Demonym:" + green + parent_dictionary['demonym'] + reset)
    print("Borders:", end=' ')
    for border_country in parent_dictionary['borders']:
        print(green + border_country + reset + ', ', end='')
    print("")
    # currencies
    print("Currencies:", end=' ')
    for currency in parent_dictionary['currencies']:
        print(green + currency['name'] + reset, end=', ')
        print(yellow + currency['code'] + reset, end=', ') 
        print(cyan + currency['symbol'] + reset, end='\n')
    print("link to flag: ", end=''); print(red + parent_dictionary['flag'] + reset)
    


# ------------------------------------------------------------------------------------------
# EXECUTIONS

# setup argparse
parser = argparse.ArgumentParser(description="Query country info")

#args = parser.add_argument('--all', '-a', help="Shows all countries and their calling codes")
args = parser.add_argument('fullname', help="Shows all countries and their calling codes", type=str, nargs='*')

args = parser.parse_args()


# This if run calls api for ALL information on ALL countries
#result = rq.get('https://restcountries.eu/rest/v2/all')
#json_payload_list = result.json()



# makes request to webAPI for country information
for arg in args.fullname:
    try:
        result = rq.get(f'https://restcountries.eu/rest/v2/name/{arg}?fullText=true')
        json_payload = result.json()
        json_payload = json_payload[0]
        print_country_information(json_payload)
    except KeyError:
        print(red + "Country not found" + reset + ": Check your spelling")
    # calls printing/formatting/highlighting function
    #print(json_payload) # uncomment to print raw json data
    
    
    






