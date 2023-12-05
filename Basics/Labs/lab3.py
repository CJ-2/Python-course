import datetime
def display_menu(menu):
    print('MENU:')
    x = 1
    for key,value in menu.items():
        print(str(x)+'.'+key+' price:'+str(value))
        x+=1
def order(menu,orders):
    display_menu(menu)
    choice = ''
    while choice == '':
        choice = input('enter your choice:')
        if choice=='1':
            orders.append('Burger')
            print('item added')
        elif choice=='2':
            orders.append('Pizza')
            print('item added')
        elif choice=='3':
            orders.append('French fries')
            print('item added')
        elif choice=='4':
            orders.append('Salad')
            print('item added')
        else:
            print('invalid input')
    choice = input('do you want to order (y/n)')
    if choice.lower() == 'y':
        order(menu,orders)
def total_price(menu,orders):
    total = 0
    for i in orders:
        total += menu.get(i)
    return str(total)
def invoice(menu,orders,invoice_text,id):
    order(menu,orders)
    total = total_price(menu,orders)
    with open('Textfile/invoices.txt','a') as file:
        text = invoice_text.format(id,orders,total,datetime.datetime.now())
        file.write(text+'\n-------------------')
def read_invoices():
    with open('Textfile/invoices.txt','r') as file:
        print(file.read())
def main():
    menu = {'Burger':10,
        'Pizza':25,
        'French fries':34,
        'Salad':8
       }
    orders = []
    invoice_text = '\nid:{}\norder:{}\ntotal price:{}\ntime:{}'
    id =0
    choice = ''
    while choice!=3:
        id+=1
        print('Restaurant:\n1.Order\n2.Orders list\n3.exit')
        choice = int(input('enter your choice:'))
        if choice==1:
            invoice(menu,orders,invoice_text,id)
        elif choice==2:
            read_invoices()
        elif choice ==3:
            print('exit...')
        else:
            print('invald input')
main()