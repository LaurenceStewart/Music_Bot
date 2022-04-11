
def check_phone(question, ph_low, ph_high):
    while True: # sets up while loop
        try:
            num = int(input(question)) # expect customer input is integer
            test_num = num 
            count = 0
            while test_num > 0:
                test_num = test_num//10
                count = count+1
            if count >= ph_low and count <= ph_high: # if number entered between 7 and 10 it will print it
                return str(num)                
            else: # if number entered is not between 7 and 10 it will print message
                print("NZ phone number have between 7 and 10 digits")
        except ValueError: # if input is not a number
            print("Try again")

question = ("Please enter you phone number ")
ph_low = 7 # lowest number is 7
ph_high = 10 # highest number is 10
phone = check_phone(question, ph_low, ph_high)
print(phone)    