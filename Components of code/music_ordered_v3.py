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

#ask total number of pizzas for order
num_items = 0

while True:
    try:
        num_items = int(input("How many items do you want to order? "))
        if num_items >= 1 and num_items <=12:
            break
        else:
            print ("Your order must be between 1 and 12 items")
    except ValueError:
        print("That is not a valid number")
        print("Please enter a number between 1 and 12")


#Choose pizza from menu
for item in range(num_items):
    while num_items > 0:
        while True:
            try: 
                items_ordered = int(input("Please choose what item or items by entering the number from the menu "))
                if items_ordered >= 1 and items_ordered <=12:
                    break
                else:
                    print("Your item must be between 1 and 12")
            except ValueError:
                    print("That is not a valid number")
                    print("Please enter a number between 1 and 12")
        items_ordered = items_ordered -1
        order_list.append(music_names[items_ordered])
        order_cost.append(music_prices[items_ordered])
        print("{} ${:.2f}"  .format(music_names[items_ordered],music_prices[items_ordered]))
        num_items = num_items-1

print(order_list)
print(order_cost)


