class Ant(object):
	"""Ant class for IACO"""
	def __init__(self, ant_id, tabu=set()):

		self.ant_id = ant_id
		self.tabu = tabu