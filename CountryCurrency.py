# -*- coding: utf-8 -*-
import sys
import datetime
from time import sleep
import pprint

# This will always return the same object
sys.path.append('.')


class CountryCurrency:

    def __init__(self, currency_country_name, currency_alphabetic_code):
        # Variables to store OWM connection data:
        self._currency_country_name = currency_country_name
        self._currency_alphabetic_code = currency_alphabetic_code


    # Airport ID
    @property
    def currency_country_name(self):
        return self._currency_country_name

    @currency_country_name.setter
    def set_currency_country_name(self, currency_country_name):
        self._currency_country_name = currency_country_name






    # Python Class Encapsulation - Properties (getter), setters




