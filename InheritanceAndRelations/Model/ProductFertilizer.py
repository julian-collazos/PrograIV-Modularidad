from Model.ProductControl import Product


class Fertilizer(Product):
    def __init__(self, ICA, product_name, aplication_frecuency, cost, last_aplication):
        Product.__init__(self, ICA, product_name, aplication_frecuency, cost)
        self.__last_aplication = last_aplication

    @property
    def last_aplication(self):
        return self.__last_aplication

    @last_aplication.setter
    def last_aplication(self, last_aplication):
        self.__last_aplication = last_aplication
