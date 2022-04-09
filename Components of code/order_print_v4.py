#list to store ordered pizzas
order_list = ['Black Ice AC/DC # CD','Ten Peral Jam # CD','Rattle and Hum U2 # Vinyl','Greatest Hits Queen # Vinyl']
#list to store ordered prices
order_cost = [20.50, 20.50, 20.50, 40.00]

cust_details = {'name':'Laurence','phone':'098123987','house':'23','street':'Evelyn','suburb':'Howick'}

del_click = 4

del_click = 'delivery'


def print_order():
    total_cost = sum(order_cost)
    print("Customer Details")
    print(f"Customer Name: {cust_details['name']} \nCustomer Phone: {cust_details['phone']} \nCustomer Address: {cust_details['house']} {cust_details['street']} {cust_details['suburb']}")
    print()
    print("Your Order Details")
    count = 0
    for item in order_list:
        print("Ordered: {} Cost: ${:.2f}".format(item, order_cost[count]))
        count = count+1
    print()
    if del_click == "delivery":
        if len(order_list) >= 5:
            print("Your delivery charge is free")
        elif len(order_list) <= 5:
            print("A $9.00 delivery fee applies. It will be included in the total cost")
            total_cost = total_cost+9
    print()
    print("Order Cost")
    print(f"${total_cost:.2f}")


print_order()
