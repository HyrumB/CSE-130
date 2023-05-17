import random

hb_num = int(input("please input positive number"))

hb_secret = random.randint(1, hb_num)

hb_guess = "" 

hb_guess_list = []

hb_loopnum = 0

while hb_guess != hb_secret:
    hb_guess = int(input("\nguess a number between 1-20: "))

    hb_loopnum += 1

    if hb_guess <= hb_secret:
        print("\ntoo low")

    elif hb_guess >= hb_guess:
       print("\ntoo high")
    
    else:
        print("how did you end up here?")

    hb_guess_list.append(hb_guess)
    #print(f"\nlist:{hb_guess_list}")
    #print(f"secret:{hb_secret}")

    
print(f"\n\nYou were able to find the number in {len(hb_guess_list)} guesses.")
print(f"The numbers you guessed were: {hb_guess_list}")