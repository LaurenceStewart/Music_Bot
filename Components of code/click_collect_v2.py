#bug
#code accepts blank input

print ("Please enter the click and collect information below")

#customer name
valid = False
while not valid:
    name = input("Please enter your name ")
    if name != "":
        print (name)
        break
    else:
        print("Sorry this cannot be blank")

#customer mobile phone
valid = False 
while not valid:
    mobile_phone = input("Please enter your mobile phone number")
    if mobile_phone != "":
        print (mobile_phone)
        break
    else:
        print("Sorry this cannot be blank")