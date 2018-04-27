import unittest
from airportAtlas import AirportAtlas
import os

os.chdir('../')
# cwd = os.getcwd()

class TestAirportAtlas(unittest.TestCase):

    def setUp(self):
        self.filename = "airport.csv"

    def test_load_data(self):
        self.assertEqual(5275, len(AirportAtlas.load_data(self.filename)))


if __name__ == '__main__':
    print("test")
    unittest.main()