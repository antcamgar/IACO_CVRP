from ant import Ant

class Colony(object):

    def __init__(self,num_of_ants,id_colony=0):
        self.id_colony = id_colony
        if num_of_ants <= 0:
            raise ValueError("Number of ants have to be great than 0.")
        self.ants = [Ant(ant_id) for ant_id in range(num_of_ants)]

    def __str__(self):
        str_col = "Colony id: " + self.id_colony + "\n"
        str_col += "Number of ants: " + str(len(self.ants)) + "\n"
        for str_ant in map(lambda ant: str(ant),self.ants):
            str_col += str_ant
        return str_col