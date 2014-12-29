import random

class Ant(object):
	"""Ant class for IACO"""
	
	def __init__(self, ant_id, initial_node, my_colony_id,tabu=set()):
        self.ant_id = ant_id
		self.tabu = tabu
		self.current_node = initial_node
        self.my_colony_id = my_colony_id
		self.visited_nodes = list()

    def get_decision_table(self, weighted_graph, global_tabu):
    	"""
        Returns the decision table of this ant.
    	"""
    	decision_table = dict()
        node_neighbors = weighted_graph.neighbors(self.current_node)
        promising_neighbors = list()
        #losers_neighbors = list() #this list is not necessary prob 0.0!!!It's like losers were gone

        for node in node_neighbors:
            if not node in self.tabu and not node in global_tabu:
                promising_neighbors.append(node)
        
        acum = 0.0
        node_tau_eta = dict()
        for h in promising_neighbors:
            edge_current_node_to_h = weighted_graph[self.current_node][h]
            tau_ih = edge_current_node_to_h['pheromone']
            eta_ih = 1.0 / edge_current_node_to_h['weight']
            temp = tau_ih**alpha * eta_ih**beta
            node_tau_eta[h] = temp
            acum += temp

    	for next_node,influence in node_tau_eta.iteritems():
            #influence here is equal to tau_ij**alpha * eta_ij**beta on the paper
            decision_table[next_node] = (influence * 1.0) / acum

        return decision_table

    def select_next_node(self, nodes_probabilities):
    	"""
    	Returns the next node chosen by this ant according to nodes_probability and 
        "weighted lucky wheel method". Obviously, the higher probability of node j is, the higher 
        probability of this ant selects node j.
    	"""
    	cumulative_probability = 0.0
        rand_number = random.random()  # This ant spins the wheel

        for node,probability in nodes_probabilities.iteritems():
            cumulative_probability += probability
            if cumulative_probability >= rand_number:
                return node

    def update_ant(self, next_node):
    	"""Update the ant current_node, tabu set and visited_nodes
    	"""
    	self.tabu.add(next_node)
    	self.visited_nodes.append((self.current_node,next_node))
    	self.current_node = next_node

    def __str__(self):
    	str_ant = "Ant id: " + str(self.ant_id) + "\n"
        str_ant += "Current node: " + str(self.current_node) + "\n"
        str_ant += "Tabu list: " + str(self.tabu)
        
        return str_ant