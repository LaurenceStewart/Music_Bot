#list of music names
music_names = ['Black Ice, AC/DC # CD','PowerUp, AC/DC # CD','Ten, Peral Jam # CD','From the Fires, Greta Van Fleet # CD'
            ,'Hotel California, Eagles # CD','Reload, Metallica # CD','Mothership, Led Zepplin # Vinyl','Powerage, AC/DC # Vinyl'
            ,'Warning, Green Day # Vinyl','Rattle and Hum, U2 # Vinyl','Deisel and Dust, Midnight Oil # Vinyl','Greatest Hits, Queen # Vinyl']
#list of music prices
music_prices = [20.50,20.50,20.50,20.50,20.50,20.50,40.00,40.00,40.00,40.00,40.00,40.00]

#list to store ordered music
order_list =[]
#list to store music proces
order_cost =[]

#list to store order cost
def menu():
    number_items = 12

    for count in range (number_items):
        print("{} {} ${:.2f}"    .format(count+1,   music_names[count],music_prices[count]))

menu()

#ask total number of items for order
num_items = 0

num_items = int(input("How many items do you want to order? "))

print (num_items)

#Choose items from menu
print ("Please choose what item or items by entering the number from the menu")
for item in range(num_items):
    while num_items > 0:
        items_ordered = int(input())
        order_list.append(music_names[items_ordered])
        order_cost.append(music_prices[items_ordered])
        num_items = num_items-1

print(order_list)
print(order_cost)


