#list to store ordered pizzas
order_list = ['Black Ice AC/DC # CD','Ten Peral Jam # CD','Rattle and Hum U2 # Vinyl','Greatest Hits Queen # Vinyl']
#list to store ordered prices
order_cost = [20.50, 20.50, 20.50, 40.00]

cust_details = {'name':'Laurence','phone':'098123987','house':'23','street':'Evelyn','suburb':'Howick'}


def print_order():
    total_cost = sum(order_cost)
    print("Customer Details")
    print(f"Customer Name: {cust_details['name']} \nCustomer Phone: {cust_details['phone']} \nCustomer Addres: {cust_details['house']} \nCustomer Street: {cust_details['street']} \nCustomer Suburb: {cust_details['suburb']}")
    print()
    print("Order Details")
    count = 0
    for item in order_list:
        print("Ordered: {} Cost: ${:.2f}".format(item, order_cost[count]))
        count = count+1
    print()
    print("Order Cost")
    print(f"${total_cost:.2f}")


print_order()