#list to store ordered pizzas
order_list = ['Black Ice AC/DC # CD','Ten Peral Jam # CD','Rattle and Hum U2 # Vinyl','Greatest Hits Queen # Vinyl']
#list to store ordered prices
order_cost = [20.50, 20.50, 20.50, 40.00]

cust_details = {'name':'Laurence','phone':'098123987','house':'23','street':'Evelyn','suburb':'Howick'}

#print("\n Customer name: {} Customer Phone:\n{} Customer House Number:\n{} Customer Street Name:\n{} Customer Suburb"
#     .format( cust_details['name'],cust_details['phone'],cust_details['house'],cust_details['street'],cust_details['suburb']))



print(f"{cust_details['name']} {cust_details['phone']} {cust_details['house']} {cust_details['street']} {cust_details['suburb']}")

count = 0
for item in order_list:
    print("Ordered: {} Cost ${:.2f}".format(item, order_cost[count]))
    count = count+1
