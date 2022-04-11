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
                    print()
                    break

                elif confirm == 2:
                    print("Your Order has been Cancelled")
                    print("You can restart you order or exit the BOT")
                    print()
                    break
            else: 
                print("The number must be 1 or 2")
        except ValueError:
            print ("That is not a valid input")
            print ("Please enter 1 or 2")

confirm_cancel()