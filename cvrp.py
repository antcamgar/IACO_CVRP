class Cvrp(object):
	"""Capacity Vehicle Routing Problem Class"""
	def __init__(self, customers, lengths, vehicles, vehicle_capacity):

		# Restrictions:
		# - The number of vehicles must be lesser than the number of customers.
		# - The number of vehicles multiplied by its capacity must be higher
		#	than the total quantity of customers goods.
		# - There must be a deposit.
		# - There must be at least one vehicle.	
		if (vehicles > len(customers) 
			or vehicles*vehicle_capacity < sum([c.quantity for c in customers]) 
			or [c.quantity for c in customers].count(0)!=1
			or vehicles < 1):
			
			# The problem can't be solved with these arguments.
			print("There is no solution for that problem with these arguments.")

		else:

			self.customers = customers
			self.lengths = lengths
			self.vehicles = vehicles
			self.vehicle_capacity = vehicle_capacity