#customer details dictionary
customer_details = {}

#instructions for customer
print ("Please enter the click and collect information below")

#customer name - not blank
valid = False
while not valid:
    customer_details['name'] = input("Please enter your name ")
    if customer_details ['name'] != "":
        print (customer_details['name'])
        break
    else:
        print("Sorry this cannot be blank")

#customer mobile phone - not blank
valid = False 
while not valid:
    customer_details['mobile_phone'] = input("Please enter your mobile phone number ")
    if customer_details['mobile_phone'] != "":
        print (customer_details['mobile_phone'])
        break
    else:
        print("Sorry this cannot be blank")

print (customer_details)