class Customer():
	"""Customer class for CVRP"""
	def __init__(self, id_customer,quantity):
        self.id_customer = id_customer
		if quantity < 0:
			raise ValueError("Quantity of goods required by the customer can't be negative.")
		else:
			self.quantity = quantity


    def __str__(self):
        str_customer = "Customer id: " + str(self.id_customer) + "\n"
        str_customer = "Quantity: " + str(self.quantity) + " goods\n"
        return str_customer


