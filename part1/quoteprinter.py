# Mini Project: Motivational Quote Printer
# Description

# Create a simple Python program that displays a random motivational quote each time it runs.


# ---------------------------------------------------------------------------------------------




import random

print("=== Motivational Quote Printer ===")

quotes = [
    "Believe you can and you're halfway there.",
    "Keep pushing forward, no matter what.",
    "Dream big. Start small. Act now.",
    "Don’t watch the clock; do what it does. Keep going.",
    "The harder you work for something, the greater you’ll feel when you achieve it."
]

# Randomly select a quote
quote = random.choice(quotes)

print(f"\n💬 {quote}")




# ================================================================================================

# Try It Yourself:

# Add more quotes to the list.

# Ask the user for their name and personalize the message.

# Save the quotes in a text file and load them dynamically.