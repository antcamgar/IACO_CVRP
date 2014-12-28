class IacoProblem():
    

    def __init__(self, alpha, beta, matrix_distances, n_ants, nodes, q0, rho, tau0):

        if (rho <= 0 or rho > 1
        	or q0 < 0 or q0 > 1):

        	print("Wrong range of arguments for IACO algorithm.")

        else:
            self.alpha = alpha
            self.ants = dict()
            for x in range(k):
                self.ants["ant" + str(x)] = Ant(x,set())
        	self.beta = beta
            self.distances_table = matrix_distances
            self.nodes = nodes
            self.pheromone_table = distances_table
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

        
    def local_search(self):

    
    def mutation(self):

        
    def node_probability(self, i, j, ant):
        
        if j in ant.tabu:
            return 0.0
        else:
            return (pheromone_table[i][j] ** alpha) * (distances_table[i][j] ** beta) / (
                sum[(pheromone_table[i][h] ** alpha) * (distances_table[i][h] ** beta) 
                    for h in range(n) if not h in ant.tabu])


    def update_pheromone(self):
        