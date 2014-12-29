from ant import Ant
from customer import Customer

class Colony(object):

    def __init__(self,num_of_ants,colony_id=0):
        self.colony_id = colony_id
        if num_of_ants <= 0:
            raise ValueError("Number of ants have to be great than 0.")
        self.ants = [Ant(ant_id,Customer(0,0),colony_id) for ant_id in range(num_of_ants)]
        #Moparia cmabiar elcustomer hay pero ahoramismo estoy frito para pensar otro modelo
        #mañana pensamos

    def __str__(self):
        str_col = "Colony id: " + self.colony_id + "\n"
        str_col += "Number of ants: " + str(len(self.ants)) + "\n"
        for str_ant in map(lambda ant: str(ant),self.ants):
            str_col += str_ant
        return str_col