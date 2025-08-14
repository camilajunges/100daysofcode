# Data types, numbers, operations, type conversions and f-strings

# subscripting
from calendar import c
from operator import length_hint
import string


print("Hello"[3])

# string
print("123" + "4 ")

# integer
print(123 + 456)

# large integer
print(123_456_789) # just to visualize better because the terminal ignore the _

# float
print(123.45)

# boolean
print(True)
print(False)



# Type error, type checking and type conversion
print(type(123))

number = 123456789
string_number = str(number)
qtd_dig = len(string_number)
print(f"The number {number} has {qtd_dig} digits.")

print(int("123") + int("456"))

print("Number of letters in your name: " + str(len(input("Enter your name: "))))

#or 
user_name = input("Enter your name: ")
name_length = len(user_name)

print(type("Number of letters in your name: "))
print(type(name_length))

print("Number of letters in your name: " + str(len(input("Enter your name: "))))


# calculate BMI 

height = 1.65
weight = 84

bmi = weight / (height **2)

print(round(bmi, 2))


# f-strings and number manipulation

score = 0
height = 1.8
is_winning = True

print(f"Your score is: {score}, your height is {height} and you winning is: {is_winning}")