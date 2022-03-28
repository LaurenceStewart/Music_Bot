import sys

#list to store ordered music
order_list =[]
#list to store music proces
order_cost =[]

#customer details dictionary
customer_details = {}
def new_exit():
        print ("Do you want to start another order or exit? ")
        print ("To start another order enter 1")
        print ("To exit the BOT enter 2")
        print()


        while True:
            try:    
                confirm = int(input("Please enter a number "))
                if confirm >= 1 and confirm <= 2:
                    if confirm == 1: 
                        print("New Order")
                        print()
                        order_list.clear()
                        order_cost.clear()
                        customer_details.clear()
                        main()
                        break

                    elif confirm == 2:
                        print("Exit")
                        print()
                        order_list.clear()
                        order_cost.clear()
                        customer_details.clear()
                        sys.exit
                        break
                else: 
                    print("The number must be 1 or 2")
            except ValueError:
                print ("That is not a valid input")
                print ("Please enter 1 or 2")


def main():
    print("Restart")

new_exit()