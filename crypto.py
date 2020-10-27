#!/usr/bin/python3.4
#-*- coding: utf-8-*-
# ==============================================================================
# title           :crypto.py                                                   #
# description     :Return the price of crypto                                  #
# author          :Odka33 - Elie BEN AYOUN                                     #
# date            :12/04/2018                                                  #
# version         :0.1                                                         #
# usage           :python3 crypto.py                                           #
# python_version  :3.4.3                                                       #
# ==============================================================================

import cryptocompare
import time
import os

os.system("figlet crypto")
print("#############################################")
time.sleep(0.2)
print("#############################################")


def chooseCoinCurrency():
    coin = str(input("Choose Currency: EUR, USD: "))
    currency = str(input("Choose Coin: BTC, ETH, XMR.. : "))
    print('You choose correctly ' +coin+ ' and ' +currency+ '!')  
    g = print(cryptocompare.get_price(coin, curr=currency, full=False))
    print("Q if you won't to exit")  
    
def listAllDevise():
    g = cryptocompare.get_coin_list(format=False)
    for key, value in g.items():
        print(key)
    print("Q if you won't to exit")

def Choose():
    value = input("If you won't to see list of crypto input Y/N/Q : ")
    while True:    
        if value == 'N':
            chooseCoinCurrency()
        if value == 'Y':
            listAllDevise()
        if value == 'Q':
            break
Choose()

  



