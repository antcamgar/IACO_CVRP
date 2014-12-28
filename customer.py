class Customer():
	"""Customer class for CVRP"""
	def __init__(self, q):

		if q < 0:
			print("The quantity of goods required by the customer can't be negative.")
		else:
			self.quantity = q