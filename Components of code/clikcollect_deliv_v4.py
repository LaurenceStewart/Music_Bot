#menu so that customer can choose click and collect or delivery

print ("Would you like to click and collect your order or have it delivered?")

print ("For click and collect enter 1")
print ("For delivery enter 2")


low = 1
high = 2

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