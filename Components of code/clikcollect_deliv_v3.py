#menu so that customer can choose click and collect or delivery
#Bug
#code needs to be programed so that it only accepts 1 or 2 as input

print ("Would you like to click and collect your order or have it delivered?")

print ("For click and collect enter 1")
print ("For delivery enter 2")

while True:
    try:    
        delivery = int(input("Please enter a number "))
        if delivery == 1:
            print("Click and collect")
        
        elif delivery == 2:
            print("Delivery")

    except ValueError:
        print ("That is not a valid input")
        print ("Please enter 1 or 2")
