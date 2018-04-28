# -*- coding: utf-8 -*-
import sys
import datetime
from time import sleep
from aircraft import Aircraft
from load_aircraft import LoadAircraft
from airportAtlas import AirportAtlas
from data_cleanse import DataCleanse
from user_input import UserInput


import pprint


def main():
    """Main method for airplane"""

    country_c, currency_c, airport_c, aircraft_c = DataCleanse.initialize()

    DataCleanse.start_clean()

    #print(airport_c.airport_cc_df.head(n=3))

    # Initialize the Airport class:

    print()

    airports_dict = AirportAtlas.load_data(airport_c.airport_file_merged)
    KJFK = airports_dict['JFK']

    print('Number of airports initialized:', len(airports_dict))
    # KJFK.tostring()

    aircraft_dict = LoadAircraft.load_data(aircraft_c.aircraft_file_clean)
    print()
    print('Number of aircraft initialized:', len(aircraft_dict))
    # aircraft_dict['BAE146'].tostring

    print()
    print()

    new_input = UserInput(airports_dict)

    new_input.desc_program()
    new_input.itinerary_size()
    new_input.itinerary_input()


if __name__ == "__main__":

    sys.exit(main())
