# Mini Project: Guess-the-Number Game
# Project Description

# Create a game where:

# The computer chooses a random number.

# The player guesses until they get it right.

# The program gives hints (“too high” or “too low”).



import random

print("=== Guess the Number Game ===")

# Step 1: Generate random number
secret_number = random.randint(1, 20)

# Step 2: Initialize variables
attempts = 0

# Step 3: Loop until correct guess
while True:
    guess = int(input("Guess a number between 1 and 20: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Correct! The number was {secret_number}.")
        print(f"You guessed it in {attempts} tries.")
        break  # Exit the loop




# ====================================================================================

# Try It Yourself:

# Limit the number of guesses to 5 attempts.

# Add an option to play again.

# Use different difficulty levels (e.g., 1–10, 1–50).