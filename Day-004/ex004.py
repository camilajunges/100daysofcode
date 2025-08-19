# Randomisation and Python lists
import random #is a module

# random_integer = random.randint(0, 3)
# print(random_integer)

# module (module.py)
# import on the top of the file
# print(module.favorite_number) file of the module . function/variable

random_number = random.random() * 10
print(random_number)
# Creates a random float in the range [0.0,1.0). You have to do an extra step, multiplying by 10, to change the range.


random_float = random.uniform(1, 10)
print(random_float)
# random.uniform(a, b): Creates a random float in the range [a,b], which is exactly what you did with random.uniform(1, 10).


head_tail = random.randint(0,1)
if head_tail == 0:
    print("Heads")
else:   
    print("Tails")


# Lists - data structure
# fruis = [item1, item2] 

states  = ["Delaware", "Pensylvannia", "Michigan", "New Jersey", "Georgia"]
states.append("Camilinda")
print(states)

################################## exercise 
# import random
print("Who will pay the bill??")

friends = ["Anna", "Sabine", "Charlie", "Emanuel", "Beatrice"]
chosen = random.choice(friends)
print(f"The one who's gonna pay the bill is: {chosen}")
