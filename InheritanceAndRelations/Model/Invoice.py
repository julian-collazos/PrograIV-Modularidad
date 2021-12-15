class Bill():
    def __init__(self, date, price, id_bill):
        self.__id_bill = id_bill
        self.__date = date
        self.__price = price
        self.__products = []

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def id_bill(self):
        return self.__id_bill

    @id_bill.setter
    def id_bill(self, id_bill):
        self.__id_bill = id_bill

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, product):
        self.__products.append(product)

    def associate(self, product):
        self.products.append(product)
