# loops
# for item in list_of_items:
#   #do something

fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)


####### ex 1: what is the total score
scores  = [150, 127, 32, 64, 192, 200, 87, 47, 50, 51]
total = sum(scores)
# sum = 0
max_score = 50
for score in scores:
    if score > max_score:
        print(":)")
    else: 
        print(":(")
    

# print(sum)
# print(max(scores))
# print(min(scores))


### loops with range() function
## for number in range(a, b): print(number)


for number in range(1,11, 3):
    print(number)

# Gauss Challenge
total = 0
for numberr in range(1,101):
   total += numberr
   print(numberr)

# You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:

# Your program should print each number from 1 to 100 in turn and include number 100.
# But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"


for div in range(1, 101):
    if div % 3 == 0 and div % 5 == 0:
        print("FizzBuzz")
    elif div % 3 == 0:
        print("Fizz")
    elif div % 5 == 0:
        print("Buzz")
    else:
        print(div)
