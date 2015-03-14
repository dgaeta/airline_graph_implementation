import random
import unittest
from City import *

class TestCity(unittest.TestCase):

    def setUp(self):
    	self.city = City("SFO", "San Francisco", "United States", "North America", "WST", {10, 10}, 1234, 1)
         
  	def test_city_code(self):
  		self.assertEqual("SFO", self.city.code)

  	def test_city_name(self):
  		self.assertEqual("San Francisco", self.city.name)

    def test_city_country(self):
      	self.assertEqual("United States", self.city.country)

    def test_city_continent(self):
      	self.assertEqual("North America", self.city.continent)

    def test_city_timezone(self):
      	self.assertEqual("WST", self.city.timezone)

    def test_city_timezon(self):
      	self.assertEqual({10,10}, self.city.coordinates)

    def test_city_coordinates(self):
    	self.assertEqual(1234, self.city.population)

    def test_city_population(self):
        self.assertEqual(1, self.city.region)


if __name__ == '__main__':
    unittest.main()