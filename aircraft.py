# -*- coding: utf-8 -*-
import sys
import datetime
from time import sleep
import pprint

# This will always return the same object
sys.path.append('.')

class Aircraft:

    def __init__(self, aircraft_code, aircraft_type, aircraft_units, aircraft_manufacturer, aircraft_range):
        # Variables to store OWM connection data:
        self._aircraft_code = aircraft_code
        self._aircraft_type = aircraft_type
        self._aircraft_units = aircraft_units
        self._aircraft_manufacturer = aircraft_manufacturer
        self._aircraft_range = aircraft_range

    # Python Class Encapsulation - Properties (getter), setters
    @property
    def aircraft_code(self):
        return self._aircraft_code

    # aircraft_type:
    @property
    def aircraft_type(self):
        return self._aircraft_type

    # Aircraft_standard:
    @property
    def aircraft_units(self):
        return self._aircraft_units

    # aircraft_manufacturer:
    @property
    def aircraft_manufacturer(self):
        return self._aircraft_manufacturer

    # aircraft_range:
    @property
    def aircraft_range(self):
        return self._aircraft_range

    @aircraft_range.setter
    def aircraft_range(self, aircraft_range):
        self._aircraft_range = aircraft_range

    @property
    def tostring(self):
        print(self._aircraft_code, self._aircraft_type, self._aircraft_units, self.aircraft_manufacturer, self._aircraft_range)
        return


