class Client():
    def __init__(self, account_number, client_name):
        self.__id_number = account_number
        self.__name = client_name
        self.__bills = []

    @property
    def id_number(self):
        return self.__id_number

    @id_number.setter
    def id_number(self, id):
        self.__id_number = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def bills(self):
        return self.__bills

    @bills.setter
    def bills(self, bill):
        self.__bills.append(bill)

    def associate(self, bill):
        self.bills.append(bill)


def add_client(clients_list, id_number):
    name = input("please enter your name: ")
    person = Client(id_number, name)
    clients_list.append(person)
    return clients_list
