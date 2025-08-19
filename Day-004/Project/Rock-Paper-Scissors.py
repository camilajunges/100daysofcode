import random

print("Let's play rock, paper, scissors!")
print("0 = Rock, 1 = Paper, 2 = Scissors")
print("---")

try:
    player_choice = int(input("Choose a number (0, 1, 2): "))
except ValueError:
    print("You did not enter a number.")
    exit()

if player_choice not in [0, 1, 2]:
    print("Invalid number. Please choose 0, 1, or 2.")
else:
    computer_choice = random.randint(0, 2)
    
    options = ["Rock", "Paper", "Scissors"]
    print(f"You chose: {options[player_choice]}")
    print(f"The computer chose: {options[computer_choice]}")
    print("---")
    
    if player_choice == computer_choice:
        print("It's a draw!")
    elif (player_choice == 0 and computer_choice == 2) or \
         (player_choice == 1 and computer_choice == 0) or \
         (player_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose.")