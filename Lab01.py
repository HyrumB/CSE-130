# 1. Name: 
#    Hyrum J. Bullock : 2023-4-17

# 2. Assignment Name: 
#    Lab 01: Python Review

# 3. Assignment Description:
#    this program makes a simple guessing game where you input a number and it then picks a random number 
#   between 1 and the number you picked 

# 4. What was the hardest part? Be as specific as possible.
#    the hardest part was formatting the code into the outline as it broke a few of the lines and i had to rewrite it slightly 

# 5. How long did it take for you to complete the assignment?
#    around 1 hour and 30 minutes  


#At the first prompt, select the value 1. Guess 1 on your first attempt.
#At the first prompt, select the value 1. Guess 0, then 2, then 1.
#At the first prompt, select the value 10 and play the game the best you can.
#At the first prompt, select the value 50 and play the game the best you can.



import random

# Game introduction.
print("This is the \"guess a number\" game.")
print("You try to guess a random number in the smallest number of attempts.")

# Prompt the user for how difficult the game will be. Ask for an integer.
hb_num_max = int(input("\nplease input positive number: "))

# Generate a random number between 1 and the chosen value.
hb_rand_num = random.randint(1, hb_num_max)

# Give the user instructions as to what he or she will be doing.
print(f"Guess a number between 1 and {hb_num_max}")

# Initialize the sentinal and the array of guesses.
hb_guess = "" 
hb_guess_list = []
hb_loopnum = 0

# Play the guessing game.
while hb_guess != hb_rand_num:

    # Prompt the user for a number.
    hb_guess = int(input(f"> "))

    # Store the number in an array so it can be displayed later.
    hb_guess_list.append(hb_guess)

    # Make a decision: was the guess too high, too low, or just right.
    if hb_guess < hb_rand_num:
        print("\ttoo low")

    elif hb_guess > hb_rand_num:
       print("\ttoo high")

# Give the user a report: How many guesses and what the guesses where.
print(f"\nYou were able to find the number in {len(hb_guess_list)} guesses.")
print(f"The numbers you guessed were: {hb_guess_list}")