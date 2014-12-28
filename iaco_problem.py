

class IacoProblem(object):
    

    def __init__(self, alpha, beta, d, k, n, q0, rho, tau0):

        if (rho <= 0 or rho > 1
        	or q0 < 0 or q0 > 1):

        	print("Wrong range of arguments for IACO algorithm.")

        else:

        	self.alpha = alpha
        	self.beta = beta
            self.distances = d
            self.k = k
            self.nodes = n
        	self.q0 = q0
        	self.rho = rho
        	self.tau0 = tau0

        
    def local_search(self):

    
    def mutation(self):
        

    def update_pheromone(self):
        