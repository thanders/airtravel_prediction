# -*- coding: utf-8 -*-
import sys
import os
import csv

import datetime
from time import sleep
import pprint

from CountryCurrency import CountryCurrency

# This will always return the same object
sys.path.append('.')
cwd = os.getcwd()


class CCAtlas:

    @staticmethod
    def load_data(filename):
        country_currency = {}

        with open(os.path.join(cwd, "data_files", filename),
                  "rt", encoding="utf8") as f:

            reader = csv.reader(f)

            for row in reader:
                currency_country_name = row[15]
                # remove cr
                country_currency[currency_country_name] =\
                    CountryCurrency(row[15], row[14])
        return country_currency


    # Python Class Encapsulation - Properties (getter), setters




