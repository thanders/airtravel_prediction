# -*- coding: utf-8 -*-
import sys
import datetime
from time import sleep
from aircraft import Aircraft
from airport import Airport
from CCAtlas import CCAtlas
from airportAtlas import AirportAtlas
import pprint

# This will always return the same object
sys.path.append('.')

def main():
    """Console script for led_tester."""

    # Initalize the Airport class:

    filename = "airport.csv"
    airports = AirportAtlas.load_data(filename)
    KJFK = airports['KJFK']

    print(KJFK.airportName, KJFK.airportID, KJFK.country, KJFK.code)
    print()
    # Initalize the CountryCurrency class:
    filename = "countrycurrency.csv"
    CC = CCAtlas.load_data(filename)

    US = CC['UNITED STATES'].currency_country_name
    print(US)

    return 0


if __name__ == "__main__":
    sys.exit(main())
