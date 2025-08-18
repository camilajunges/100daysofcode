print("Welcome to the Python Pizza Delivery")
size = input("What size of pizza do you want: S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? y or n: ")
extra_cheese = input("Do you want extra cheese on your pizza? y or n: ")
bill = 0

# to do: work out how much they need to pay based on their size choice

# to do: work out how much to add to their bill based on pepperoni choice

# to do: work out their finel amount based on whether they want extra cheese

# small = $15 - medium = $20 - large = $25 
# pepperoni for small pizza = +$2, medium = +$4 - large = +$6
# extra cheese for small pizza = +$2, medium = +$4 - large = +$6

if size == "S":
    bill = 15
    if pepperoni == "Y":
        bill = bill + 2
    elif extra_cheese == "Y":
        bill + 2
    else: bill = 15
if size == "M":
    bill = 20
    if pepperoni == "Y":
        bill = bill + 2
    elif extra_cheese == "Y":
        bill + 2
    else: bill = 20
if size == "L":
    bill = 25 
    if pepperoni == "Y":
        bill = bill + 2
    elif extra_cheese == "Y":
        bill + 2
    else: bill = 25

print(f"We'll prepare your pizza! Your bill is: {bill}")
