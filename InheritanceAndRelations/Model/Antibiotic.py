class Antibiotic():
    def __init__(self, animal_type, product_name, dose, price):
        self.__animal_type = animal_type
        self.__product_name = product_name
        self.__dose = dose
        self.__price = price

    @property
    def animal_type(self):
        return self.__animal_type

    @animal_type.setter
    def animal_type(self, animal_type):
        self.__animal_type = animal_type

    @property
    def product_name(self):
        return self.__product_name

    @product_name.setter
    def product_name(self, product_name):
        self.__product_name = product_name

    @property
    def dose(self):
        return self.__dose

    @dose.setter
    def dose(self, dose):
        self.__dose = dose

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price
