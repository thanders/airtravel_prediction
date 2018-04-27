# -*- coding: utf-8 -*-
import sys
import os
import csv

from aircraft import Aircraft

# This will always return the same object
sys.path.append('.')
cwd = os.getcwd()


class LoadAircraft:

    @staticmethod
    def load_data(filename):
        aircraft_dict = {}
        with open(os.path.join("", "clean_files", filename),
                  "rt", encoding="utf8") as f:

            reader = csv.reader(f)

            for row in reader:
                aircraft_code = row[0]
                # remove cr
                aircraft_dict[aircraft_code] =\
                    Aircraft(row[0], row[1], row[2], row[3], row[4])
        return aircraft_dict


    # Python Class Encapsulation - Properties (getter), setters




