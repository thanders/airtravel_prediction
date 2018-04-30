# -*- coding: utf-8 -*-
import sys
import datetime
from time import sleep
import pprint

# This will always return the same object
sys.path.append('.')


class Airport:

    def __init__(self, iata_code, icao_code, latitude, longitude, country, airportName, cityName, to_EUR, currency_code):
        # Variables to store OWM connection data:
        self.iata_code = iata_code
        self.icao_code = icao_code
        self.latitude = latitude
        self.longitude = longitude
        self.country = country
        self.airportName = airportName
        self.cityName = cityName
        self.to_EUR = to_EUR
        self.currency_code = currency_code

    def tostring(self):
        print(self.icao_code, self.country, self.cityName, self.airportName, self.latitude, self.longitude, self.to_EUR, self.currency_code)

    # Python Class Encapsulation - Properties (getter), setters




