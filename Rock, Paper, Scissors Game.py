import random

choices = ["rock", "paper", "scissors"]

def decide_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "You win! 🎉"
    else:
        return "Computer wins! 😔"

while True:
    player_choice = input("Choose rock, paper or scissors: ").lower()
    if player_choice not in choices:
        print("Invalid choice. Try again.")
        continue

    comp_choice = random.choice(choices)
    print(f"Computer chose: {comp_choice}")
    print(decide_winner(player_choice, comp_choice))

    again = input("Play again? (y/n): ").lower()
    if again != 'y':
        print("Game over. GG! ✌️")
        break
