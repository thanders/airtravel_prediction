# -*- coding: utf-8 -*-
import sys
import datetime
from time import sleep
import pprint

# This will always return the same object
sys.path.append('.')


class Airport:

    def __init__(self, airportID, airportName, cityName, country, code, ICAOcode, latitude, longitude, altitude, timeOffset, dst, tz):
        # Variables to store OWM connection data:
        self._airportID = airportID
        self.airportName = airportName
        self._cityName = cityName
        self._country = country
        self._code = code
        self._ICAOcode = ICAOcode
        self._latitude = latitude
        self._longitude = longitude
        self._altitude = altitude
        self._timeOffset = timeOffset
        self._dst = dst
        self._tz = tz

# Airport ID
    @property
    def airportID(self):
        return self._airportID

    @airportID.setter
    def set_airportID(self, airportID):
        self._airportID = airportID

# Airport Country name:
    @property
    def country(self):
        return self._country

    @airportID.setter
    def set_country(self, country):
        self._country = country

    # Airport Country name:
    @property
    def code(self):
        return self._code

    @airportID.setter
    def set_code(self, code):
        self._code = code


    def print(self):
        print(self._airportID, self.airportName, self._cityName, self._country, self._code, self._ICAOcode, self._latitude, self._longitude, self._altitude, self._timeOffset, self._dst, self._tz)

    # Python Class Encapsulation - Properties (getter), setters




