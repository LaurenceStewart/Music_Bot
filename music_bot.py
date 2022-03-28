#music bot program
#23/3/22 
#bugs
#phone number allows numbers
#name inout allows numbers

import sys
import random
from random  import randint

#list of random names
names = ["Laurence", "George", "Toby", "Caleb", "Matthew", "Josh", "Terry", "Zach", "Luke", "Oscar"]
#list of music names
music_names = ['Black Ice AC/DC                 # CD','PowerUp AC/DC                   # CD','Ten Peral Jam                   # CD','From the Fires Greta Van Fleet  # CD'
            ,'Hotel California Eagles         # CD','Reload Metallica                # CD','Mothership Led Zepplin          # Vinyl','Powerage AC/DC                  # Vinyl'
            ,'Warning Green Day               # Vinyl','Rattle and Hum U2              # Vinyl','Deisel and Dust Midnight Oil   # Vinyl','Greatest Hits Queen            # Vinyl']
#list of music prices
music_prices = [20.50,20.50,20.50,20.50,20.50,20.50,40.00,40.00,40.00,40.00,40.00,40.00]

#list to store ordered music
order_list =[]
#list to store music proces
order_cost =[]

#customer details dictionary
customer_details = {}


#validated inputs to check if they are blank
def not_blank(question):
    valid = False
    while not valid:
        response = input(question)
        if response != "":
            return response.title()
        else: 
            print("This cannot be blank")


#welcome message
def welcome():
    '''
    Purpose: to generate a random name from the list and print out a welcome message
    Parameters: none
    Returns: none
    '''
    num = randint(0,9)
    name = (names[num])
    print("#### Welcome to Groovey Music ####")
    print("#### My name is",name, "####")
    print("#### I am here to help you order music albums of your choice ####")


#menu for clikc and collect or delivery option
def order_type():
    del_click = ""
    print ("Would you like to click and collect your order or have it delivered?")
    print ("For click and collect enter 1")
    print ("For delivery enter 2")
    while True:
        try:    
            delivery = int(input("Please enter a number "))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print("Click and collect")
                    del_click = 'click and collect'
                    clickcollect_info()
                    break
            
                elif delivery == 2:
                    print("Delivery")
                    delivery_info()
                    del_click = 'delivery'
                    break
            else:
                print("The number entered must be 1 or 2")

        except ValueError:
            print ("That is not a valid input")
            print ("Please enter 1 or 2")
    return del_click


#Click and collect information - name and mobile phone
def clickcollect_info():
    question = ("Please enter you name ")
    customer_details['name'] = not_blank(question)
    print (customer_details['name'])

    question = ("Please enter you mobile phone number ")
    customer_details['mobile_phone'] = not_blank(question)
    print (customer_details['mobile_phone'])
    print()


#Delivery information - name, address, phone number
def delivery_info():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question)
    print (customer_details['name'])

    question = ("Please enter you phone number ")
    customer_details['phone'] = not_blank(question)
    print (customer_details['phone'])

    question = ("Please enter you house number ")
    customer_details['house'] = not_blank(question)
    print (customer_details['house'])

    question = ("Please enter you street name ")
    customer_details['street'] = not_blank(question)
    print (customer_details['street'])

    question = ("Please enter you suburb ")
    customer_details['suburb'] = not_blank(question)
    print (customer_details['suburb'])
    print()


#Music menu
def menu():
    number_items = 12

    for count in range (number_items):
        print("{} {} ${:.2f}"  .format(count+1,music_names[count],music_prices[count]))


#Choose total number of music items
    #Music items order, code to print items and cost from menu
def order_music():

    #ask total number of pizzas for order
    num_items = 0

    while True:
        try:
            num_items = int(input("How many items do you want to order? "))
            if num_items >= 1 and num_items <=12:
                break
            else:
                print ("Your order must be between 1 and 12 items")
        except ValueError:
            print("That is not a valid number")
            print("Please enter a number between 1 and 12")


    #Choose pizza from menu
    for item in range(num_items):
        while num_items > 0:
            while True:
                try: 
                    items_ordered = int(input("Please choose what item or items by entering the number from the menu "))
                    if items_ordered >= 1 and items_ordered <=12:
                        break
                    else:
                        print("Your item must be between 1 and 12")
                except ValueError:
                        print("That is not a valid number")
                        print("Please enter a number between 1 and 12")
            items_ordered = items_ordered -1
            order_list.append(music_names[items_ordered])
            order_cost.append(music_prices[items_ordered])
            print("{} ${:.2f}"  .format(music_names[items_ordered],music_prices[items_ordered]))
            num_items = num_items-1


#print order out
    #include if for click and collect or delivery (and users information for those options)
def print_order():
    total_cost = sum(order_cost)
    print("Customer Details")
    print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']} \nCustomer Addres: {customer_details['house']} \nCustomer Street: {customer_details['street']} \nCustomer Suburb: {customer_details['suburb']}")
    print()
    print("Order Details")
    count = 0
    for item in order_list:
        print("Ordered: {} Cost: ${:.2f}".format(item, order_cost[count]))
        count = count+1
    print()
    print("Order Cost")
    print(f"${total_cost:.2f}")

#ability to cancel or proceed with order
def confirm_cancel():
    print ("Please confirm your order below")
    print ("To confirm please enter 1")
    print ("To cancel please enter 2")

    while True:
        try:    
            confirm = int(input("Please enter a number "))
            if confirm >= 1 and confirm <= 2:
                if confirm == 1: 
                    print("Order Confirmed")
                    print("Your order has been sent to our store for processing")
                    break

                elif confirm == 2:
                    print("Your Order has been Cancelled")
                    print("You can restart you order or exit the BOT")
                    break
                else: 
                    print("The number must be 1 or 2")
        except ValueError:
            print ("That is not a valid input")
            print ("Please enter 1 or 2")


#Option for new order or to exit the program
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



# Main function
def main():
    '''
    Purpose: To run all functions
    a welcome message
    Parameters: none
    Returns: none
    '''
    welcome()
    del_click = order_type()
    menu()
    order_music()
    print_order(del_click)
    confirm_cancel()


main()