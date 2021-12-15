class Product():
    def __init__(self, ICA, product_name, aplication_frecuency, cost):
        self.__ICA = ICA
        self.__product_name = product_name
        self.__aplication_frecuency = aplication_frecuency
        self.__price = cost

    @property
    def ICA(self):
        return self.__ICA

    @ICA.setter
    def ICA(self, ICA):
        self.__ICA = ICA

    @property
    def product_name(self):
        return self.__product_name

    @product_name.setter
    def product_name(self, product_name):
        self.__product_name = product_name

    @property
    def aplication_frecuency(self):
        return self.__aplication_frecuency

    @aplication_frecuency.setter
    def aplication_frecuency(self, aplication_frecuency):
        self.__aplication_frecuency = aplication_frecuency

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price
