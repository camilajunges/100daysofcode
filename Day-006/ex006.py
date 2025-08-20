# Functions

print("Hello")
num_char = len("Hello")
print(num_char)

# make our own function - def

def function(): # model to create function
    print("Hello")
    print("Bye")


# call the function

function()

# def function():
#   do this
#   then do this
#   finally do this

# function()
# aut exercises

def sum_numbers():
     return a + b

a = int(input("Choose a number: "))
b = int(input("Choose another number: "))

print(f"The sum between {a} and {b} is: {sum_numbers(a, b)}")


# while loops
#for item in list_of_items:
#   do somthings

#while somethins_is_true:
#   do something

count = 1 
while count <= 5:
    print(count)
    count += 1


name = ""
while not name:
    name = input("Whats your name: ")
print(f"Hello, {name}")



number = 0
while number < 10:
    number += 1
    if number % 2 == 0:
        continue 
    print(number)