from Model.ProductControl import Product


class Pest(Product):
    def __init__(self, ICA, product_name, aplication_frecuency, cost, grace_period):
        Product.__init__(self, ICA, product_name, aplication_frecuency, cost)
        self.__grace_period = grace_period

    @property
    def grace_period(self):
        return self.__grace_period

    @grace_period.setter
    def grace_period(self, grace_period):
        self.__grace_period = grace_period
