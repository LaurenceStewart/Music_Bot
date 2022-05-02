# music bot program
# 23/3/22 - date main code was created
# bugs
# phone number allows numbers
# name inout allows numbers

import sys
import random
from random import randint
from turtle import st

PH_LOW = 7  # lowest number is 7
PH_HIGH = 10  # highest number is 10

# list of random names
names = ["Laurence", "George", "Toby", "Caleb", "Matthew", "Josh", "Terry", "Zach", "Luke", "Oscar"]
# list of music names
music_names = ['Black Ice AC/DC                 # CD', 'PowerUp AC/DC                   # CD', 'Ten Peral Jam                   # CD', 'From the Fires Greta Van Fleet  # CD'
                , 'Hotel California Eagles         # CD', 'Reload Metallica                # CD', 'Mothership Led Zepplin          # Vinyl', 'Powerage AC/DC                  # Vinyl'
                , 'Warning Green Day               # Vinyl', 'Rattle and Hum U2              # Vinyl', 'Deisel and Dust Midnight Oil   # Vinyl', 'Greatest Hits Queen            # Vinyl']

# list of music prices
music_prices = [20.50, 20.50, 20.50, 20.50, 20.50, 20.50, 40.00, 40.00, 40.00, 40.00, 40.00,40.00]  # prices correspond to music names

# list to store ordered music
order_list =[]  # this is where the ordered music items will be stored, in a list
# list to store music prices
order_cost =[]  # this is where the ordered music items cost will be stored, in a list

# customer details dictionary
customer_details = {}  # this is where the customers information will be stored


# validated inputs to check if they are blank
def not_blank(question):  # function to check blank inputs and print not blank message
    valid = False
    while not valid:
        response = input(question)  # asks for input
        if response != "":  # if response is blank print error message
            return response.title()  # if true returns response 
        else: 
            print("This cannot be blank")  # this cannot be blank message

def check_string(question):  # function to check for numbers in inputs that should only contain letters
    while True:  # sets up while loop
        response = input(question)
        x = response.isalpha()
        if x is False:
            print("Input must only contain letters")  # error message
        else:
            return response.title()  # returns response and makes sure the first letter entered is a capital and rest are lowercase

def check_phone(question, PH_LOW, PH_HIGH):
    while True:  # sets up while loop
        try:
            num = int(input(question))  # expect customer input is integer
            test_num = num
            count = 0
            while test_num > 0:
                test_num = test_num//10
                count = count + 1
            if count >= PH_LOW and count <= PH_HIGH:  # if number entered between 7 and 10 it will print it
                return str(num)  # returns string to variable, question 
            else:  # if number entered is not between 7 and 10 it will print message
                print("NZ phone numbers have between 7 and 10 digits")
        except ValueError:  # if input is not a number
            print("Try again")

# welcome message
def welcome():  # function to print a welcome message to the customer
    # what the code does, if it has any parameters or returns
    '''
    Purpose: to generate a random name from the list and print out a welcome message 
    Parameters: none
    Returns: none
    '''
    num = randint(0,9)  # random integer within 0 - 9, this is how many random names are in the list
    name = (names[num])  # name generated corresponds to randint or random number in line above
    print()
    print("#### Welcome to Groovey Music ####")
    print("#### My name is" , name , "####")  # prints message with random name from list
    print("#### I am here to help you order music albums of your choice ####")
    print()


# menu for click and collect or delivery option
def order_type():
    del_click = ""
    print ("Would you like to click and collect your order or have it delivered?")
    print ("1 For click and collect ")
    print ("2 For delivery ")
    print()
    while True:  # sets up while loop
        try:    
            delivery = int(input("Please enter a number "))  # variable, expected input will be an integer
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:  # if delivery (variable) is 1
                    print("Click and collect")
                    print()
                    del_click = 'click and collect'  # variable is for click and collect 
                    clickcollect_info()  # runs click and collect info function
                    break  # exits out of the loop
            
                elif delivery == 2:  # elif delivery (variable) is 2
                    print("Delivery")
                    print()
                    del_click = 'delivery'  # variable is for delivery
                    delivery_info()  # runs delivery info function
                    break  # exits out of the loop
            else:  # something other than a number is entered
                print("The number entered must be 1 or 2")
        except ValueError:  # a number other than 1 or 2 is entered
            print ("That is not a valid input")
            print ("Please enter 1 or 2")
    return del_click  # returns the variable del_click


# Click and collect information - name and mobile phone
def clickcollect_info():  # function to collect customers click and collect information
    question = ("1 Please enter your name ")  # question for customers name
    customer_details['name'] = check_string(question)  # input stored in dictionary, blank input run def check_string
    print (customer_details['name'])  # print customers entered name
    print()

    question = ("2 Please enter your mobile phone number ")  # question for customers mobile phone number
    customer_details['mobile_phone'] = check_phone(question, PH_LOW, PH_HIGH)  # input stored in dictionary, blank input run def check_phone 
    print (customer_details['mobile_phone'])  # prints customers entered mobile phone number
    print()


# Delivery information - name, address, phone number
def delivery_info():  # function to collect customers delivery information
    question = ("1 Please enter your name ")  # question for customers name
    customer_details['name'] = check_string(question)  # input stored in dictionary, blank input run def check_string
    print (customer_details['name'])  # prints customers entered name
    print()

    question = ("2 Please enter your phone number ")  # question for customers phone number
    customer_details['phone'] = check_phone(question, PH_LOW, PH_HIGH)  # input stored in dictionary, blank input run def check_phone
    print (customer_details['phone'])  # prints customers entered phone number
    print()

    question = ("3 Please enter your house number ")  # question for customers house number
    customer_details['house'] = not_blank(question)  # input stored in dictionary, blank input run def not_blank
    print (customer_details['house'])  # prints customers entered house number
    print()

    question = ("4 Please enter your street name ")  # question for customers street name
    customer_details['street'] = check_string(question)  # input stored in dictionary, blank input run def check_string
    print (customer_details['street'])  # prints customer entered street name
    print()

    question = ("5 Please enter your suburb ")  # question for customers suburb
    customer_details['suburb'] = check_string(question)  # input stored in dictionary, blank input run def check_string
    print (customer_details['suburb'])  # prints customers entered suburb
    print()


# Music menu
def menu():  # function to print menu items and their prices
    number_items = 12  # number of items on the menu that will be printed

    print("Item list")
    for count in range(number_items):
        print("{} {} ${:.2f}"  .format(count+1,music_names[count],music_prices[count]))  # prints item menu with prices (2 decimal places)


# Choose total number of music items
# Music items order, code to print items and cost from menu
def order_music():  # function to see how many items the customer wants to order
    # ask total number of items for orders
    num_items = 0
    while True:  # sets up while loop
        try:
            print()
            num_items = int(input("How many items do you want to order? "))  # variable, expected input will be an integer
            if num_items >= 1 and num_items <=12:
                break  # exits out of loop
            else:  # if something other than a number is entered
                print ("Your order must be between 1 and 12 items") 
        except ValueError:  # if a number below 1 or above 12 is entered
            print("That is not a valid number")
            print("Please enter a number between 1 and 12")


    # Choose pizza from menu
    for item in range(num_items):
        while num_items > 0:
            while True:  # sets up while loop
                try: 
                    print()
                    items_ordered = int(input("Please choose what item or items by entering the number from the menu "))  # expected input will be a integer
                    if items_ordered >= 1 and items_ordered <=12:  # if integer entered is larger than 1 and smaller than 12
                        break  # exits out of loop
                    else:  # if something other than a number is entered
                        print("Your item must be between 1 and 12")
                except ValueError:  # if a number below 1 or above 12 is entered
                        print("That is not a valid number")
                        print("Please enter a number between 1 and 12")
            items_ordered = items_ordered -1
            order_list.append(music_names[items_ordered])
            order_cost.append(music_prices[items_ordered])
            print("{} ${:.2f}"  .format(music_names[items_ordered],music_prices[items_ordered]))  # prints selected items with cost from lists
            num_items = num_items-1


# print order out
# include if for click and collect or delivery (and users information for those options)
# 'print()' are to add spaces between lines when the code is run
def print_order(del_click):  # function to print out order information and customer details
    total_cost = sum(order_cost)  # variable total_cost is sum(order_cost), which is music_prices added up     
    if del_click == 'click and collect':  # if parameter click and collect, prints customer details for click and collect from customer_details dictionary 
        print() 
        print("Your order if for Click and Collect")
        print()
        print("Your Details")
        print(f"1 Customer Name: {customer_details['name']} \n2 Customer Phone: {customer_details['mobile_phone']}")
        print()  # the line above gets customers information from the dictionary and prints it for the customer to see
        print("You will receive a text message when your item/s are ready to be picked up")
        print()
    elif del_click == 'delivery':  # if parameter is delivery, prints customer details for delivery from customer_details dictionary
        print()
        print("Your order is for delivery")
        print(f"1 Customer Name: {customer_details['name']} \n2 Customer Phone: {customer_details['phone']} \n3 Customer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
        print()  # the line above gets customers information from the dictionary and prints it for the customer to see
# line break
    print("Your Order Details")
    count = 0
    for item in order_list:
        print("Ordered: {} Cost: ${:.2f}".format(item, order_cost[count]))  # prints out all items customer has ordered with their costs from the lists
        count = count+1
    print()
    if del_click == "delivery":
        if len(order_list) >= 5:  # if variable is delivery and order is for 5 or more items there is no delivery fee
            print("Your delivery charge is free")  # tells customer about delivery fee
            print()
        elif len(order_list) <= 5:  # elif variable is delivery and order is for 4 or less items, delivery fee is $9.00
            print("A $9.00 delivery fee applies. It will be included in the total cost")  # tells customer about delivery fee
            print()
            total_cost = total_cost+9  # adds $9.00 to total cost 
    print("Total Order Cost")
    print(f"${total_cost:.2f}")  # prints total order cost to 2 decimal places, with dollar sign
    print()


# ability to cancel or proceed with order
def confirm_cancel():  # function to confirm or cancel the order

    print ("Please confirm your order below")  # gives the user options to choose, tells user what they are
    print ("1 To confirm order")
    print ("2 To cancel order")
    print()

    while True:  # sets up while loop
        try:
            confirm = int(input("Please enter a number "))  # variable, expected input will be a integer
            if confirm >= 1 and confirm <= 2:  # if statement for customer input
                if confirm == 1:  # if the variable input is 1
                    print("Order Confirmed")
                    print("Your order has been sent to our store for processing")
                    print()
                    new_exit()  # runs new_exit function
                    break  # exits out of loop

                elif confirm == 2:  # elif the variable input is 2
                    print("Your Order has been Cancelled")
                    print("You can restart you order or exit the BOT")
                    print()
                    new_exit()  # runs new_exit function
                    break  # exits out of loop
            else:  # something other than a number is entered
                print("The number must be 1 or 2")
        except ValueError:  # a number below 1 or above 2 is entered
            print ("That is not a valid input")
            print ("Please enter 1 or 2")



# Option for new order or to exit the program
def new_exit():  # function to allow customer to exit program or start new order
        print ("Do you want to start another order or exit? ")  # gives user options to choose, tells them what they are
        print ("1 To start another order")
        print ("2 To exit the BOT")
        print()

        while True:  # sets up while loop
            try:
                confirm = int(input("Please enter a number "))  # variable, expected input will be an integer
                if confirm >= 1 and confirm <= 2:  # if statement for customer input
                    if confirm == 1:  # if the customer inout is 1
                        print("New Order")  # tells customer what option they selected
                        print()
                        order_list.clear()  # clears the order_list list, what customer ordered
                        order_cost.clear()  # clears the order_cost list how much each item was
                        customer_details.clear()  # clears customer_details dictionary or customers information
                        main()  # returns to main function, starts program again for new order
                        break  # exits out of loop

                    elif confirm == 2:  # elif the customer input is 2
                        print("Exit")  # tells customer what option they selected
                        print()
                        order_list.clear()  # clears the order_list list, what customer ordered
                        order_cost.clear()  # clears the order_cost list, how much each item was
                        customer_details.clear()  # clears customer_details dictionary of customers information
                        sys.exit  # exits the program
                        break  # exits our of loop
                else:  # something other than a number was entered
                    print("The number must be 1 or 2")
            except ValueError:  # a number below 1 or above 2 was entered
                print ("That is not a valid input")
                print ("Please enter 1 or 2")



# Main function
def main():  # this is the main function, it is used in the new_exit function to run the program again if customer wants new order
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
