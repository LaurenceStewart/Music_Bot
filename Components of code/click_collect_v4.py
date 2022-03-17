#customer details dictionary
customer_details = {}

def not_blank(question):
    valid = False 
    while not valid: 
        response = input(question)
        if response != "":
            return response.title()
        else: 
            print("This cannot be blank")


#instructions
question = ("Please enter you name ")
customer_details['name'] = not_blank(question)
print (customer_details['name'])

question = ("Please enter you mobile phone number ")
customer_details['mobile_phone'] = not_blank(question)
print (customer_details['mobile_phone'])


print (customer_details)