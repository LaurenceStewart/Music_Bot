#music bot program
#23/3/22
#bugs
#phone number allows numbers
#name inout allows numbers

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
                    break
            
                elif delivery == 2:
                    print("Delivery")
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
