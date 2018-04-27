# -*- coding: utf-8 -*-
import sys
import datetime
from time import sleep
from aircraft import Aircraft
from load_aircraft import LoadAircraft
from airportAtlas import AirportAtlas
from data_cleanse import DataCleanse
import pprint


def main():
    """Main method for airplane"""

    country_c, currency_c, airport_c, aircraft_c = DataCleanse.initialize()

    DataCleanse.start_clean()

    #print(airport_c.airport_cc_df.head(n=3))

    # Initialize the Airport class:

    print()

    airports_dict = AirportAtlas.load_data(airport_c.airport_file_merged)
    KJFK = airports_dict['KJFK']

    print('Number of airports initialized:', len(airports_dict))

    print('Example:')
    KJFK.tostring()

    aircraft_dict = LoadAircraft.load_data(aircraft_c.aircraft_file_clean)
    print()
    print('Number of aircraft initialized:', len(aircraft_dict))
    print('Example:')
    aircraft_dict['BAE146'].tostring

    print()
    print()

    itinerary_set = set([])

    loop = True

    print("Please enter four destinations (airport ICAO codes).")
    print("The first code you enter is your destination")
    try:

        while loop:
            air_code = str(input("Input code:"))

            if (air_code not in itinerary_set) and len(itinerary_set) < 3:
                itinerary_set.add(air_code)
                print("Set", itinerary_set, "Size:", len(itinerary_set))
                print()

            elif len(itinerary_set) == 3:
                itinerary_set.add(air_code)
                print("Set", itinerary_set, "Size:", len(itinerary_set))
                print()
                print("Thank-you, I will now calculate the shortest path (fuel price weighted)")
                loop = False

            else:
                print("Sorry that one is already in the set")

            # raise ValueError("Sorry, I don't understand your input")


    # except ValueError as e:
    #    print(e)
    #    main()

    except KeyboardInterrupt:
        print()
        print("Goodbye!!")
        exit()

    except Exception as e:
        print(e)







if __name__ == "__main__":
    sys.exit(main())
