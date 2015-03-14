""" @author Danny Gaeta 
	see superclass: Graph 
"""

from Graph import *
import webbrowser
import unicodedata

class AirlineGraph(Graph):
	"""docstring for AirlineGraph"""
	def __init__(self, json_file):
		Graph.__init__(self, json_file)



	def get_info(self, city_code, requested_info):
		return self.vertices[city_code][requested_info]

	def get_all_cities(self):
		city_list = []
		for key in self.vertices:
			city_list.append(self.vertices[key]["name"] + " " + key)
		return city_list


	# opens the gcmap.com website in default browser 
	def open_mapper(self):
		url = "http://www.gcmap.com/mapui?P="
		params = ""
		for key in self.adj_list:
			for dest in self.adj_list[key]:
				route_string = "+" + key.encode('ascii','ignore') + "-" + dest.encode('ascii','ignore') + ","
				params += route_string
		edit = bytearray(params)
		del edit[0]
		del edit[-1]
		params = str(edit)
		url += params
		webbrowser.open(url, new=0)

	def remove_city(self, city_code):
		for item in self.adj_list:
			try:
				self.adj_list[item].remove(city_code)
			except ValueError, e:
				pass

		try:
			del(self.vertices[city_code])
			return True
		except KeyError, e:
			return False

		
	def remove_route(self, endpoints):
		try:
			self.adj_list[endpoints[0]].remove(endpoints[1])
			return True 
		except ValueError, e:
			return False

	def add_city(self, city):
		if self.vertices[str(city.code)]:
			return False

		self.vertices[city.code] = {"code":city.code, "name":city.name, "country":city.country, 
			"continent":city.continent, "timezone":city.timezone, "coordinates":city.coordinates, 
			"population":city.population,"region":city.region
		}
		return True

	def add_route(self, endpoints, distance):
		try:
			self.adj_list[endpoints[0]].append(endpoints[1])
		except KeyError, e:
			pass
		self.distances[(endpoints[0],endpoints[1])] = distance
	
	def edit_city(self, city_code, data_field, data_value):
		try:
			self.vertices[city_code][data_field] = data_value
		except KeyError, e:
			pass #raise

	# see JSON module 
	def write_to_json(self):
		output_dict = {}
		metros_list = []
		routes_list = []

		for key in self.vertices:
			item = self.vertices[key]
			metros_list.append(item)

		for key in self.adj_list:
			for dest in self.adj_list[key]:
				endpoints = [key, dest]
				distance = self.distances[(key, dest)]
				route_format = {"ports": endpoints, "distance":distance}
				routes_list.append(route_format)

		output_dict = {"metros": metros_list, "routes": routes_list}
		json_str = json.dumps(output_dict).decode('unicode-escape').encode('utf8')
		with open('output.json', 'w') as f:
			json.dump(json_str, f)

	# First leg of trip is 35 cents per kilometer 
	# Any leg thereafter is 30 cents per kilometer
	def cost_of_route(self, route_list):
		leg = 1 
		total_cost = 0
		cost_per_k = 0.35

		origin = route_list[0]
		del(route_list[0])

		while len(route_list) >= 1:
			dest = route_list[0]
			del(route_list[0])

			if leg == 2:
				cost_per_k -= 0.5 

			if dest in self.adj_list[origin]:
				distance = self.distances[(origin, dest)]
				total_cost += (cost_per_k * distance)
			else:
				return False

			leg += 1 
			origin = dest 

			return total_cost


	def shortest_path(self, origin, dest):
		#vertices = 
		visited_set = [origin]
		unvisited_set = [key for key in self.vertices if key != origin]





		
	


				
		