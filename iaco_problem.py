

class IacoProblem(object):
    

    def __init__(self, alpha, beta, d, k, n, q0, rho, tau0):

        if (rho <= 0 or rho > 1
        	or q0 < 0 or q0 > 1):

        	print("Wrong range of arguments for IACO algorithm.")

        else:

        	self.alpha = alpha
            self.ants = dict()
            for x in range(k):
                self.ants["ant"+str(x)] = Ant(x,[])
        	self.beta = beta
            self.distances = d
            self.nodes = n
        	self.q0 = q0
        	self.rho = rho
        	self.tau0 = tau0

    def construct_route(self):

        
    def local_search(self):

    
    def mutation(self):
        
    def node_probability(self, i, j):

        # Comprobar si el nodo j está en la lista tabú general
        # si -> return 0 (probabilidad 0)
        # no
        # |
        # --> Comprobar si está en la tabla tabú de la hormiga
        #       si -> return 0 (probabilidad 0)
        #       no -> calcular la probabilidad con la formula del paper

    def update_pheromone(self):
        