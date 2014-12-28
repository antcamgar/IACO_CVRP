

class IacoProblem(object):
    

    def __init__(self, alpha, beta, q0, rho, tau0):
        
        ## NOTA: creo que el parametro q0 no es necesario porque para escapar
        ## de minimos locales ya tenemos lo de la feromona minima y maxima.

        if (rho <= 0 or rho > 1
        	or q0 < 0 or q0 > 1):

        	print("Wrong range of arguments for IACO algorithm.")

        else:

        	self.alpha = alpha
        	self.beta = beta
        	self.q0 = q0
        	self.rho = rho
        	self.tau0 = tau0

        
    def local_search(self):
        
    
    def mutation(self):
        

    def update_pheromone(self):
        