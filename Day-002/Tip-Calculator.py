print("Welcome to the tip calculator!")
print("#################################")

bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

tip_percent = tip / 100
total_tip_amount = bill * tip_percent
total_bill = bill + total_tip_amount
per_person = total_bill / people
total_amount = round(per_person, 2)

print(f"Each person should pay: ${total_amount}")

