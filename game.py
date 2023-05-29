import random

player = input("Enter your choice (rock, paper, scissors): ")
valid_options = ["rock", "paper", "scissors"]
computer = random.choice(valid_options)
print(f"\nYou chose {player}, computer chose {computer}.\n")

if player == computer:
    print(f"Both players selected {player}. It's a tie!")
elif player == "rock":
    if computer == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif player == "paper":
    if computer == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif player == "scissors":
    if computer == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
else:
    print(f"{player} is an invalid option. Play again.")




















