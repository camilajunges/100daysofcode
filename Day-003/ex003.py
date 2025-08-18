# conditional statements, logical operators, code blocks and scope
import this
from tkinter import Y


print("See if you got the enough height here.")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You have height enough!")
else:
    print("Sorry you don't have height enough...")



# modulo operator (how many is remaining after the division)
# Write some code using modulp op and conditional checks to check if the number in the input area is odd or even. If it's odd print the word 'odd' otherwise print 'even'

number = int(input("Write a number: "))
if number % 2 == 0:
  print('Odd')
else:
  print('Even')


# Nested if statements and elif statement (aninhado) 
print("Welcome to the rollercoaster!")
height = int(input("What's your age in cm? "))
age = int(input("And what's your age? "))

if height >= 120:
    print("You have height enough!")
    if age < 12:
      print("You can ride the rollercoaster, your ticket will cost $5.")
    elif 12 <= age <= 18:
      print("You can ride the rollercoaster, your ticket will cost $7.")
    else: 
      print("You can ride the rollercoaster, your ticket will cost $12.")
else:
    print("Sorry you don't have height enough... Maybe next time!")


# Calculate and interpretate bmi

print("Hello, let's calculate your bmi!")
weight = 85
height = 1.85

bmi_calc = weight / (height **2)
bmi = round(bmi_calc, 1)
if bmi < 18.5:
  print(f"Your bmi is: {bmi}, you are underweight.")
elif 18.5 <= bmi <= 24.9:
  print(f"Your bmi is: {bmi}, you are normal.")
else:
  print(f"Your bmi is {bmi}, you are overweight.")


# Multiple if statement in succesion
print("Welcome to the rollercoaster!")
height = int(input("What's your age in cm? "))
age = int(input("And what's your age? "))
bill = 0

if height >= 120:
    print("You have height enough!")
    if age < 12:
      bill = 5
      print(f"Your ticket will cost ${bill}.")
    elif 12 <= age <= 18:
      bill = 7
      print(f"Your ticket will cost ${bill}.")
    else: 
      bill = 12
      print(f"Your ticket will cost ${bill}.")

    wants_photo = input("Do you want to have a photo taken? y or n: ")
    if wants_photo == "y":
      
      bill += 3
    
    print(f"Your bill will be: ${bill}")

      
else:
    print("Sorry you don't have height enough... Maybe next time!")
    