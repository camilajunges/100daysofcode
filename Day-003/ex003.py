# conditional statements, logical operators, code blocks and scope
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