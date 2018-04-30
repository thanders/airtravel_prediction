# -*- coding: utf-8 -*-
import sys
import datetime
from time import sleep
from aircraft import Aircraft
from load_aircraft import LoadAircraft
from airportAtlas import AirportAtlas
from data_cleanse import DataCleanse
from user_input import UserInput
from path_calculation import PathCalculation


import pprint


def obtain_coordinates(unordered_itinerary, airports_dict):
    # Loop through dictionary
    for i in unordered_itinerary:
        # Obtain instance of class for each i in unordered_itinerary
        airport_obj = airports_dict[i]
        unordered_itinerary[i] = (airport_obj.latitude, airport_obj.longitude)

    return unordered_itinerary

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

    unordered_itinerary = new_input.itinerary_dict

    # Call function to add coordinates to the unordered_itinerary dictionary
    unordered_itinerary = obtain_coordinates(unordered_itinerary, airports_dict)

    # Create an instance of the PathCalculation class
    path_calc = PathCalculation(unordered_itinerary)

    shortest_path, price = path_calc.create_permutations()

    print("Shortest path (cheapest flight):", shortest_path, "EUR", price)

if __name__ == "__main__":

    sys.exit(main())
