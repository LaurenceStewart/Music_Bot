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