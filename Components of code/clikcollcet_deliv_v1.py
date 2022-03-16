#menu so that customer can choose click and collect or delivery
#Bug
#Code accepts anything, not just 1 or 2

print("Would you like to click and collect your order or have it delivered?")

print("For click and collect enter 1, for delivery enter 2")

delivery = input()
if delivery == "1":
    print("Click and collect")

elif delivery == "2":
    print("Delivery")
