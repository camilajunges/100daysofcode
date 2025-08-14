#print function
print('Hello World!')


# Write a program that uses print statements to print the following recipe into the Output console. The text to print is already there, you just need to make it into code. Your code should print all five lines exactly the same as the example output below. Make sure that you don't change any of these existing text as everything, punctuation and casing all need to match!

print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")

# another way to print more than 1 line above the other

print("Hello World!\nMy name is Camila!")

# concatenation strings
print("My name is Camila!" + " What's your name?")


#Look at the code in the code editor. There are errors on all 5 lines of code. Fix the code so that it runs without errors. Try to run the code and debug each line using the error messages and feedback.
print("Notes from Day 1")
print("The print statement is used to output strings")
print("Strings are strings of characters")
print("String Concatenation is done with the + sign")
print("New lines can be created with a \ and the letter n")


# input function
print("Hello, my name is Camila!")
name = input("What's your name?")
print("Hello, " + name + "!")


# variables
name = input("What's your name?")
print("Hello, " + name)


#We have 2 variables glass1 and glass2. glass1 contains milk and glass2 contains juice. Write 3 lines of code to switch the contents of the variables. You are not allowed to type the words "milk" or "juice". You are only allowed to use variables to solve this exercise.

glass1 = "milk"
glass2 = "juice"
 
temp = glass1
glass1 = glass2
glass2 = temp

print(f"glass1 agora contém: {glass1}")
print(f"glass2 agora contém: {glass2}")

# temp is a temporary variable which is commonly used to make changes in the code, just like we did with the glasses.

# naming variables
# -> make your code readable (your variables need to be consistent)