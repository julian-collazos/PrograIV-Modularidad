import Model.Methods as general_methods
import Model.Client as client_methods
import Ui.VisualMethods as visual

products = []  # [0] = control products [1] = antibiotics
clients = []

number_client = input("Please enter your id number: ")
person = general_methods.search_client(number_client, clients)
if person == -1:
    clients = client_methods.add_client(clients, number_client)
    person = general_methods.search_client(number_client, clients)

while True:
    option = general_methods.valid_option(1)
    if option == 0:
        print("Have a nice day!!")
        break
    elif option == 1:
        invoice = general_methods.billing()
        client_methods.Client.associate(person, invoice)
    else:
        visual.show_bills(clients)


