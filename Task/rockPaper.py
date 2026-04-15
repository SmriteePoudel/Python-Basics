import random
choices = ["rock","paper","scissors"]
while True:
    user = input("Enter your choice(or 'quit'):").lower()
    if user=="quit":
        print("Game Finished ")
        break
    computer = random.choice(choices)
    print("Computer choice:",computer)

    if user == computer:
        print("Tie")
    elif (
    (user == "rock" and computer == "scissors") or
    (user == "paper" and computer == "rock") or
    (user == "scissors" and computer == "paper")
):
        print("You win")
    else:
        print("You lose")    