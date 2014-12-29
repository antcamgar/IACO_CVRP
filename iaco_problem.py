class IacoProblem(object):
    

    def __init__(self, colony, weighted_graph, nodes, alpha, beta, rho, tau0, q0=-1):
        if rho <= 0 or rho > 1:
            raise ValueError("Evaporation coefficient rho is out of range.")
        
        self.alpha = alpha
        self.beta = beta
        self.ants = dict()
        for x in range(n_ants):
            self.ants["ant" + str(x)] = Ant(x)
        self.distances_table = matrix_distances
        self.nodes = nodes
        self.pheromone_table = matrix_distances

        for i in range(len(distances_table)):
            for j in range(len(distances_table[0])):
                if j != i:
                    pheromone_table[i][j] = tau0
                else:
                    pheromone_table[i][j] = 0.0
    	self.q0 = q0
    	self.rho = rho
    	self.tau0 = tau0

    def construct_route(self): 
        pass
        
    def local_search(self):
        pass
    
    def mutation(self):
        pass
        
    def node_probability(self, i, j, ant):
        
        if j in ant.tabu:
            return 0.0
        else:
            return (pheromone_table[i][j] ** alpha) * (distances_table[i][j] ** beta) / (
                sum[(pheromone_table[i][h] ** alpha) * (distances_table[i][h] ** beta) 
                    for h in range(n) if not h in ant.tabu])


    def update_pheromone(self):
        pass
