import random
import unittest
from AirlineGraph import *

class TestGraphFuntions(unittest.TestCase):

    def setUp(self):
        self.graph = AirlineGraph("test_network.json")
        self.routes = [["SCL", "LIM"]]
        self.vertices = {"SCL":
        	{
			"code" : "SCL" ,
			"name" : "Santiago" ,
			"country" : "CL" ,
			"continent" : "South America" ,
			"timezone" : -4 ,
			"coordinates" : {"S" : 33, "W" : 71} ,
			"population" : 6000000 ,
			"region" : 1
			}, "LIM": {
			"code" : "LIM" ,
			"name" : "Lima" ,
			"country" : "PE" ,
			"continent" : "South America" ,
			"timezone" : -5 ,
			"coordinates" : {"S" : 12, "W" : 77} ,
			"population" : 9050000 ,
			"region" : 1
			} 
		}

    def test_vertices_construction(self):
        # make sure the graph is constructed corrected
        self.assertEqual(2, len(self.graph.vertices))
        self.assertEqual(8, len(self.graph.vertices["SCL"]))
        self.assertEqual(8, len(self.graph.vertices["LIM"]))

    def test_adj_list_construction(self):
    	self.assertEqual("LIM", self.graph.adj_list["SCL"][0])
        

if __name__ == '__main__':
    unittest.main()