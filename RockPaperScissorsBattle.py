Here's a Python code for a simple Rock, Paper, Scissors game:

```python
import random

# Define the choices and corresponding ASCII art
choices = ["Rock", "Paper", "Scissors"]

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Get the user's choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))

# Check if the user's choice is valid
if user_choice < 0 or user_choice > 2:
    print("Invalid choice. Please choose 0, 1, or 2.")
else:
    # Generate a random choice for the computer
    computer_choice = random.randint(0, 2)

    # Display the choices
    print("Your choice:")
    if user_choice == 0:
        print(rock)
    elif user_choice == 1:
        print(paper)
    else:
        print(scissors)

    print("Computer's choice:")
    if computer_choice == 0:
        print(rock)
    elif computer_choice == 1:
        print(paper)
    else:
        print(scissors)

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose!")
```

Copy and paste this code into a Python environment to play the game. It will display the ASCII art for both the user's and computer's choices and announce the winner.
