#list to store ordered pizzas
order_list = ['Black Ice AC/DC # CD','Ten Peral Jam # CD','Rattle and Hum U2 # Vinyl','Greatest Hits Queen # Vinyl']
#list to store ordered prices
order_cost = [20.50, 20.50, 20.50, 40.00]


count = 0
for item in order_list:
    print("Ordered: {} Cost ${:.2f}".format(item, order_cost[count]))
    count = count+1
