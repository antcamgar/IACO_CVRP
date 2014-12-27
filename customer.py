class Customer(object):
	"""Customer class for CVRP"""
	def __init__(self,q):
		self.quantity = q
		self.visited = False