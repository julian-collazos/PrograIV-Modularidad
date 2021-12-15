import sys
import Ui.VisualMethods as UI
from Model import Antibiotic, Invoice, ProductFertilizer, ProductPest

def check_option(option, option_amount):
    if option < 0 or option > option_amount:
        print("Option no valid, please choose another option")
        return -1
    else:
        return option


def valid_option(section):
    option_main = 1
    option_product = 2
    invalid = -1
    while True:
        if section == option_main:
            option = UI.choose_option()
            option_amount = 2
        elif section == option_product:
            option = UI.choose_type_product()
            option_amount = 3

        if check_option(option, option_amount) != invalid:
            break
    return option



def search_client(id_client, clients):
    for client in range(len(clients)):
        client_2_compare = clients[client].id_number
        if id_client == client_2_compare:
            return clients[client]
    return -1

def buy_more():
    choose = input('Do you want to buy more? S/N\n>> ')
    choose = choose.upper()
    if choose == 'S':
        return True
    else:
        return False


def billing():
    number_invoice = int(input('Please enter the invoice number: '))
    current_date = input('Enter the current date: ')
    products = []
    total = []
    while True:
        option = valid_option(2)
        if option == 1:
            atri_ant = []
            atri_ant.append(input('Enter the antibiotic name: '))
            atri_ant.append(input('Enter the type of animal(Bovine, Porcine or goat): '))
            amount = int(input('Enter the amount of products to bring: '))
            precio = int(input('Enter the antibiotic price: '))
            atri_ant.append(precio)
            atri_ant.append(input('Enter dose(between 400Kg and 600Kg): '))
            total.append(precio * amount)
            product = Antibiotic.Antibiotic(atri_ant[0], atri_ant[1], atri_ant[3], precio)
        else:
            atri_prod = []
            atri_prod.append(input('Enter the ICA: '))
            sys.stdin.flush()
            atri_prod.append(input('Enter the name of the product: '))
            amount = int(input('Enter the amount of products to bring: '))
            atri_prod.append(input('Enter the aplication frecuency (in hours)'))
            price = int((input('Enter the cost of the product: ')))
            atri_prod.append(price)

            total.append(price*amount)

            if option == 2:
                atri_prod.append(input('Enter the grace period: '))
                product = ProductPest.Pest(atri_prod[0], atri_prod[1], atri_prod[2], atri_prod[3], atri_prod[4])
            else:
                atri_prod.append((input('Enter the date of the last aplication')))
                product = ProductFertilizer.Fertilizer(atri_prod[0], atri_prod[1], atri_prod[2], atri_prod[3], atri_prod[4])
        products.append(product)
        if not buy_more():
            break

    total_cost = 0
    for cost in total:
        total_cost += cost
    invoice = Invoice.Bill(current_date, total_cost, number_invoice)
    for product in products:
        invoice.associate(product)

    return invoice

