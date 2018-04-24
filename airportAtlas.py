# -*- coding: utf-8 -*-
import sys
import os
import csv

import datetime
from time import sleep
import pprint

from airport import Airport

# This will always return the same object
sys.path.append('.')
cwd = os.getcwd()

class AirportAtlas:

    @staticmethod
    def load_data(filename):
        airports = {}

        with open(os.path.join(cwd, "data_files", filename),
                  "rt", encoding="utf8") as f:

            reader = csv.reader(f)

            for row in reader:
                airport_code = row[5]
                # remove cr
                airports[airport_code] =\
                    Airport(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
        return airports


    # Python Class Encapsulation - Properties (getter), setters




