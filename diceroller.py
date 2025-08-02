import random

def roll_dice():
    dice_faces = {
        1: "⚀",
        2: "⚁",
        3: "⚂",
        4: "⚃",
        5: "⚄",
        6: "⚅"
    }
    
    roll = random.randint(1, 6)
    print(f"You rolled: {roll} {dice_faces[roll]}")

while True:
    user_input = input("Roll the dice? (y/n): ").lower()
    if user_input == 'y':
        roll_dice()
    elif user_input == 'n':
        print("Bye! 🎲")
        break
    else:
        print("Invalid input. Type 'y' or 'n'.")
