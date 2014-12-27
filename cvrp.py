class Cvrp(object):
	"""Capacity Vehicle Routing Problem Class"""
	def __init__(self, c, l, v, cap):

		# Restrictions
		if v > len(c) or v*cap < sum(c):
			
			# Excepcion
			pass

		else:

			self.customers = c
			self.lengths = l
			self.vehicles = v
			self.vehicle_capacity = cap