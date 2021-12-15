def choose_option():
    print("What action do you want to take?")
    print("1. New invoice")
    print("2. See the invoice list")
    print("0. Exit")
    chosen = int(input('>> '))
    return chosen


def welcome():
    print("Welcome to the farm shop!!!")


def choose_type_product():
    print('Dial...')
    print('1. if the product to add is an antibiotic.')
    print('2. if the product is of pest control.')
    print('3. if the product is a fertilizer.')
    chosen = int(input('>> '))
    return chosen


def show_bills(clients):
    for client in clients:
        print("client name: ", client.name)
        for invoice in client.bills:
            print("Date: ", invoice.date)
            print("Invoice number: ", invoice.id_bill)
            for product in invoice.products:
                print(product.product_name, "\t", product.price)
            print("Total: ", invoice.price)
            print("\t\t--------------------------")
        print("\n+++++++++++++++++++++++++++++++++++++++++++++++++")
