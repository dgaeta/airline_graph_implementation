import json
from pprint import pprint


class Graph(object):
	"""docstring for Graph"""
	def __init__(self, json_file):
		super(Graph, self).__init__()
		self.vertices = {}
		self.adj_list = {}
		self.meta_data = {}
		self.distances = {}
		


		json_data = open(json_file)
		#json_data = open("cs_air.json")
		self.meta_data = {'longest flight': 0, 'shortest flight':1000000, 'average distance': 0, 'biggest city':0,
		                 'smallest city':1000000, 'average size': 0, 'continents': {}, 'hub cities': []}
		  
		data = json.load(json_data)
		  
		self.vertices = {}
		for item in data["metros"]:
			self.vertices.setdefault(item["code"], item)
			if item["population"] > self.meta_data["biggest city"]:
				self.meta_data["biggest city"] = item["name"]
			if item["population"] < self.meta_data["smallest city"]:
				self.meta_data["smallest city"] = item["name"]
			self.meta_data["average size"] += item["population"]
			cont_dict = self.meta_data["continents"].setdefault(item["continent"], {})
			city_dict = cont_dict.setdefault(item["name"], 0)
		 
		 
		self.adj_list = {}
		for item in data["routes"]:
			route_tuple = (item["ports"][0], item["ports"][1])
			self.distances[route_tuple] = item["distance"]
			metro_dest = self.adj_list.setdefault(item["ports"][0], []) # ket might already exist
			metro_dest.append(item["ports"][1])
			if item["distance"] > self.meta_data["longest flight"]:
				self.meta_data["longest flight"] = item["distance"]
			if item["distance"] < self.meta_data["shortest flight"]:
				self.meta_data["shortest flight"] = item["distance"]
				self.meta_data["average distance"] += item["distance"]
		 
		  
		# Compute the average distance and size
		self.meta_data["average size"] = self.meta_data["average size"]/len(self.vertices)
		self.meta_data["average distance"] = self.meta_data["average distance"]/len(self.adj_list)
			 
		json_data.close()

		
		#print meta_data
		#print adj_list

		# TODO!
		# hub cities 
		# interface