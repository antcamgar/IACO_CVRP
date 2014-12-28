class Cvrp(IacoProblem):
	"""Capacity Vehicle Routing Problem Class"""
	def __init__(self, customers, lengths, vehicles, vehicle_capacity,
		alpha, beta, q0, rho, tau0):

		# Restrictions:
		# - The number of vehicles must be lesser than the number of customers.
		# - The number of vehicles multiplied by its capacity must be higher
		#	than the total quantity of customers goods.
		# - There must be a deposit.
		# - There must be at least one vehicle.
		# - The initial pheromone can't be out of the pheromone range.
		tau_range = sum([x for x in lengths[0]])
		total_customers_quantity = [c.quantity for c in customers]
		if (vehicles > len(customers) 
			or vehicles*vehicle_capacity < sum(total_customers_quantity) 
			or total_customers_quantity.count(0)!=1
			or vehicles < 1
			or tau0 < vehicle_capacity/(2*tau_range)
			or tau0 > vehicle_capacity/tau_range):
			
			# The problem can't be solved with these arguments.
			print("There is no solution for that problem with these arguments.")

		else:
			super(Cvrp, self).__init__(alpha,beta,q0,rho,tau0)
			self.customers = customers
			self.lengths = lengths
			self.vehicles = vehicles
			self.vehicle_capacity = vehicle_capacity