# This script greets the user and calculates a "lucky number"
# Created by Tracy
print("Hello! I'm Tracy, and I'm here to help you!")

user_name = input("What's your name? ")

# --- MODIFIED PART STARTS HERE ---
# Prompt the user to input their favorite number
# We use int() to make sure Python knows it's a whole number for math
favorite_number = int(input("Great! What's your favorite number? "))
# --- MODIFIED PART ENDS HERE ---

print(f"Nice to meet you, {user_name}! I'm Tracy!")
# Attempt to calculate a lucky number
lucky_number = 40
print(f"Your lucky number is: {lucky_number}")
print("Have a great day from Tracy!")