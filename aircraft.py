# -*- coding: utf-8 -*-
import sys
import datetime
from time import sleep
import pprint

# This will always return the same object
sys.path.append('.')

class Aircraft:

    def __init__(self, aircraft_code, aircraft_type, aircraft_standard, aircraft_manufacturer, aircraft_range):
        # Variables to store OWM connection data:
        self._aircraft_code = aircraft_code
        self._aircraft_type = aircraft_type
        self._aircraft_units = aircraft_standard
        self._aircraft_manufacturer = aircraft_manufacturer
        self._aircraft_range = aircraft_range

    # Python Class Encapsulation - Properties (getter), setters

    # aircraft_code:

    @property
    def aircraft_code(self):
        return self._aircraft_code

    @aircraft_code.setter
    def owm_key(self, aircraft_code):
        self._aircraft_code = aircraft_code


    # aircraft_type:
    @property
    def aircraft_type(self):
        return self._aircraft_type

    @aircraft_type.setter
    def owm_city(self, aircraft_type):
        self._aircraft_type = aircraft_type

    # Aircraft_standard:
    @property
    def aircraft_standard(self):
        return self._aircraft_standard

    @aircraft_standard.setter
    def aircraft_standard(self, aircraft_standard):
        self._owm_country = aircraft_standard

    # aircraft_manufacturer:
    @property
    def aircraft_manufacturer(self):
        return self._aircraft_manufacturer

    @aircraft_manufacturer.setter
    def aircraft_manufacturer(self, aircraft_manufacturer):
        self._aircraft_manufacturer = aircraft_manufacturer

    # aircraft_range:
    @property
    def aircraft_range(self):
        return self._aircraft_range

    @aircraft_range.setter
    def aircraft_range(self, aircraft_range):
        self._aircraft_range = aircraft_range


