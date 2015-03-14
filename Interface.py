from Graph import *
from AirlineGraph import *
from City import *

class Interface(object):
	"""docstring for Interface"""

	def __init__(self):
		#super(ClassName, self).__init__()
		self.json_file = raw_input("Please enter the JSON file name: ")
		self.graph = AirlineGraph(self.json_file)

		print 'Welcome to CSAir!'
		user_input = ""
		while user_input != "20":
			
			print '-------------------------------------------'
			print 'Enter number for meta data'
			print '1. specific information for city'
			print '2. list of all the cities that CSAir flies to'
			print '3. longest single flight in the network'
			print '4. shortest single flight in the network'
			print '5. average distance of all the flights in the network'
			print '6. biggest city (by population) served by CSAir'
			print '7. smallest city (by population) served by CSAir'
			print '8. average size (by population) of all the cities served by CSAir'
			print '9. a list of the continents served by CSAir and which cities are in them'
			print '10. CSAir hub city'
			print '11. Open route visualizer'
			print '12. Edit city'
			print '13. Remove route'
			print '14. Add city'
			print '15. Remove city'
			print '16. Add route'
			print '17. Save network to json file'
			print '18. city connections'
			print '19. cost of route'
			print '20. Quit'
			print '--------------------------------------------'

			user_input = raw_input("What is your query?: ")

			if user_input == "1":
				city_code = raw_input("Enter city code: ")
				requested_info = raw_input("Enter requested info: ")
				info = self.graph.get_info(city_code, requested_info)
				print(info)
			elif user_input == "2":
				city_list = self.graph.get_all_cities()
				for city in city_list:
					print(city.encode('ascii','ignore'))
			elif user_input == "3":
				print(self.graph.meta_data["longest flight"])
			elif user_input == "4":
				print(self.graph.meta_data["shortest flight"])
			elif user_input == "5":
				print(self.graph.meta_data["average distance"])
			elif user_input == "6":
				print((self.graph.meta_data["biggest city"]).encode('ascii','ignore'))
			elif user_input == "7":
				print((self.graph.meta_data["smallest city"]).encode('ascii','ignore'))
			elif user_input == "8":
				print(self.graph.meta_data["average size"])
			elif user_input == "9":
				for key in self.graph.meta_data["continents"]:
					print(key.encode('ascii','ignore') + ":")
					for country in self.graph.meta_data["continents"][key]:
						print(country.encode('ascii','ignore'))
					print(" ")	
			elif user_input == "10":
				print(self.graph.meta_data["hub cities"])
			elif user_input == "11":
				self.graph.open_mapper()
			elif user_input == "12":
				city_code = raw_input("Enter city code: ")
				data_field = raw_input("Enter the data field to be edited: ")
				data_value = raw_input("Enter the new data value: ")
				self.graph.edit_city(city_code, data_field, data_value)
				print("EDIT SUCCESSFUL")
			elif user_input == "13":
				origin = raw_input("Enter origin city code: ")
				dest = raw_input("Enter destination city code: ")
				status = self.graph.remove_route([origin, dest])

				if status:
					print("REMOVAL SUCCESSFUL")
				else: 
					print("Route does not exist")
			elif user_input == "14":
				code = raw_input("Enter city code: ")
				name = raw_input("Enter city name: ")
				country = raw_input("Enter the country of the city: ")
				continent = raw_input("Enter the continent of the city: ")
				timezone = raw_input("Enter the city timezone: ")
				coordinates = raw_input("Enter the city coordinates: ")
				population = raw_input("Enter the city population: ")
				region = raw_input("Enter the city region: ")
				city = City(code, name, country, continent, timezone, coordinates, population, region)

				status = self.graph.add_city(city)
				if status:
					print("ADD SUCCESSFUL")
				else:
					print("City Code is not unique")
					print("ADD FAILED")
			
				
			elif user_input == "15":
				city_code = raw_input("Enter city code: ")
				status = self.graph.remove_city(city_code)
				if status:
					print("REMOVAL SUCCESSFUL")
				else: 
					print("City does not exist")
				
			elif user_input == "16":
				origin = raw_input("Enter origin city code: ")
				dest = raw_input("Enter destination city code: ")
				distance = raw_input("Enter distance between the cities: ")
				self.graph.add_route([origin, dest], distance)
				print("ADD SUCCESSFUL")
			elif user_input == "17":
				self.graph.write_to_json()
				print("SAVE SUCCESSFUL")

			elif user_input == "18":
				city_code = raw_input("Enter the city code: ")
				connections = self.graph.adj_list[city_code]
				print((self.graph.vertices[city_code]["name"]).encode('ascii','ignore') + ":")

				for city in connections:
					print((self.graph.vertices[city]["name"]).encode('ascii','ignore'))

			elif user_input == "19":
				route = raw_input("Enter list of cities: ")
				params = route.split(" ")
				distance = self.graph.cost_of_route(params)
				if not distance:
					print("No route exists")
				print(distance)





Interface()




		