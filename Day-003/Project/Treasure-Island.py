print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a crossroad. Where do you want to go?")
direction = input("Type 'left' or 'right': ")

if direction == "right":
    print("Cool! Now you have arrived in a very large field.")
    direction = input("Do you choose to wait for rescue or move on? Type 'wait' or 'move on': ")

    if direction == "wait":
        print("You were lucky! Rescue soon arrived and you went home safe and sound.")
    elif direction == "move on":
        direction = input("Oh no, you're out of food! You found some rabbits and also some mushrooms, which would you rather eat? Type 'A' or 'B': ")

        if direction == "A":
            print("You ate the rabbit but ended up getting sick and died. Game over.")
        elif direction == "B":
            print("You ate the mushroom, got high and died lying in the field. Game over.")
        else:
            print("That's not a valid option. Game over.")
    else:
        print("That's not a valid option. Game over.")
else:
    print("You fell into a hole. Game over.")