import random

class Ant(object):
	"""Ant class for IACO"""
	
	def __init__(self, ant_id, current_node, tabu=set()):
        self.ant_id = ant_id
		self.tabu = tabu
		self.current_node = current_node
		self.visit_order = list()

    def nodes_probability(self, weighted_graph):
    	"""
    	Returns a dictionary with the probability of moving to each node.
    	"""
    	results = dict() #Poner en la clave i o no?
    	i = self.current_node
    	
    	for neighbor in weighted_graph.neighbors(i):
    		j = neighbor
    		if j in self.tabu:
    			results[j] = 0.0
    		else:
    			results[j] = (weighted_graph[i][j]['weight'] ** alpha) * (weighted_graph[i][j]['pheromone'] ** beta) / (
                sum[(weighted_graph[i][h]['weight'] ** alpha) * (weighted_graph[i][h]['pheromone'] ** beta) 
                    for h in range(n) if not h in ant.tabu])

    	return results

    def select_next_node(self, probability_dict):
    	"""
    	Returns the ant probability choice of its neighbors.
    	"""
    	cumulative_probability = 0.0
    	cumulative_probability_dict = dict()

    	for node,probability in probability_dict.items():

    		if probability > 0.0:
    			cumulative_probability += probability
    			cumulative_probability_dict[node] = cumulative_probability

    	ant_probability = random.random()
    	probability_values = cumulative_probability_dict.values()
    	
    	return max(filter(lambda x: x < ant_probability,probability_values))

    def update_ant(self, next_node):
    	"""
    	Update the ant current_node, tabu set and visit_order
    	"""
    	self.tabu.add(next_node)
    	self.visit_order.append((self.current_node,next_node))
    	self.current_node(next_node)

    def __str__(self):
    	str_ant = "Ant id: " + str(self.ant_id) + "\n"
        str_ant += "Current node: " + str(self.current_node) + "\n"
        str_ant += "Tabu list: " + str(self.tabu)

        return str_ant