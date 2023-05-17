# 1. Name:
#      hyrum Bullock
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#     Tell the user the best way to get a hotel token onto Pensylvania Ave: Built following the teachers flowchart.

# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was parsing the flowchart specifially the match statment and the confusion over the fact that you never used output D.

# 5. How long did it take for you to complete the assignment?
#     3-4 hours

def main():
    own_all_green = input("\n\nDo you own all the green properties? (y/n) ")

     # Ends program if they dont own all of green.
    if (own_all_green.upper() == "N") or (own_all_green.upper() == "NO"):
        print("\nYou cannot purchase a hotel until you own")
        print("all the properties of a given color group.\n")

    # Continues the program if they do own all of the green spaces.
    else:

        # Collects input for next if statment.
        tokens_on_PA = input("\nWhat is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel) ")
        tokens_on_PA = int(tokens_on_PA)

        # Ends program if you already have a hotel on Pen AVE
        if tokens_on_PA == 5:
            print(" You cannot purchase a hotel if the property already has one.\n")
            
        else:
            # Collects input for next if statment.
            tokens_on_NCA = input("\nWhat is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel) ")
            tokens_on_NCA = int(tokens_on_NCA)

            # Ends program if you can swap the houses and hotel on PA and CA
            if tokens_on_NCA == 5:
                print("Swap North Carolina's hotel with Pennsylvania's 4 houses..\n")

            else:
                # Collects input for next if statment.
                tokens_on_PCA = input("\nWhat is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel) ")
                tokens_on_PCA = int(tokens_on_PCA)

                # Ends program if you can swap the houses and hotel on PA and PC
                if tokens_on_PCA == 5:
                    print("\nSwap North Carolina's hotel with Pennsylvania's 4 houses..\n")

                else:
                    # Collects input for next if statment.
                    hotel_token_num = input("\nHow many hotels are there to purchase? ")
                    hotel_token_num = int(hotel_token_num)

                    # Ends program if you dont have enough hotels.
                    if hotel_token_num == 0:
                        print("There are not enough hotels available for purchase at this time.\n")

                    else:
                        # Sends the variables to a function that changes it to the tokens needed to get a full tile/space
                        tokens_PA_needs = token_flop(tokens_on_PA)
                        tokens_NCA_needs = token_flop(tokens_on_NCA)
                        tokens_PCA_needs = token_flop(tokens_on_PCA)

                        #print(f"PA{tokens_on_PA} NC{tokens_on_NCA} PC{tokens_on_PCA}")

                        # This does calculations to get the number of house tokens needed to put a hotel on Pen Ave.
                        total_house_tokens_needed = tokens_PA_needs + tokens_NCA_needs + tokens_PCA_needs

                        # This does calculations to get the minimum amount of money needed to buy all the tokens needed to
                        # place all the houses and hotels to put a hotel on Pen Ave.
                        total_money_needed = (total_house_tokens_needed * 200) + 200

                        # Collects input for next if statment.
                        user_cash = input("\nHow much cash do you have to spend? " )
                        user_cash = int(user_cash)

                        # Ends program if the user doesnt have enough funds.
                        if user_cash < total_money_needed:
                            print("You do not have sufficient funds to purchase a hotel at this time.\n")

                        else:
                            # Collects input for next if statment.
                            house_token_num = input("\nHow many houses are there to purchase? ")
                            house_token_num = int(house_token_num)

                            # Ends program if user doesnt have enough houses
                            if house_token_num < total_house_tokens_needed:
                                print("There are not enough houses available for purchase at this time.\n")

                            else:
                                # checks if Nortch carlina needs more than 
                                if tokens_NCA_needs >0:
                                    # output A
                                    print(f"\nThis will cost ${total_money_needed}.")
                                    print(f"Purchase 1 hotel and {total_house_tokens_needed} house(s).")
                                    print(f"Put 1 hotel on Pennsylvania and return any houses to the bank.")
                                    print(f"Put {tokens_NCA_needs} house(s) on North Carolina.")
                                    print(f"Put {tokens_PA_needs} house(s) on Pacific.\n")

                                    # output B
                                    print(f"\nThis will cost ${total_money_needed}.")
                                    print(f"Purchase 1 hotel and {total_house_tokens_needed} house(s).")
                                    print(f"Put 1 hotel on Pennsylvania and return any houses to the bank.")
                                    print(f"Put {tokens_NCA_needs} house(s) on North Carolina.\n")
                                
                                if tokens_PCA_needs >0:
                                    # output A
                                    print(f"\nThis will cost ${total_money_needed}.")
                                    print(f"Purchase 1 hotel and {total_house_tokens_needed} house(s).")
                                    print(f"Put 1 hotel on Pennsylvania and return any houses to the bank.")
                                    print(f"Put {tokens_NCA_needs} house(s) on North Carolina.")
                                    print(f"Put {tokens_PA_needs} house(s) on Pacific.\n")

                                    #output C
                                    print(f"\nThis will cost ${total_money_needed}.")
                                    print(f"Purchase 1 hotel and {total_house_tokens_needed} house(s).")
                                    print(f"Put 1 hotel on Pennsylvania and return any houses to the bank.")
                                    print(f"Put {tokens_PA_needs} house(s) on Pacific.\n")



def token_flop(tokens_on_space):
    # This function uses a match case to turn the amount of house tokens on the 
    # tile/space into the amount of tokens needed to attain a hotel.
    match tokens_on_space:
        case 0:
            return 4
        case 1:
            return 3
        case 2:
            return 2
        case 3:
            return 1
        case 4:
            return 0
    


main()

#output D which is never used in your flowchart

#print(f"\nThis will cost ${total_money_needed}.")
#print(f"Purchase 1 hotel and {total_house_tokens_needed} house(s).")
#print(f"Put 1 hotel on Pennsylvania and return any houses to the bank.")


# test cases

# test 1: Does not own enough	 
#   inputs: no

# test 2: Poor	 
#   inputs: yes, 0, 0, 0, 10, 100, 15

# test 3: No houses	
#   inputs: yes, 0, 0, 0, 10, 9000, 10

# test 4: Swap with Pacific	
#   inputs: yes, 4, 4, 5, 10, 0, 0

# test 5: Swap with NC
#   inputs: yes, 4, 5, 4, 10, 0, 0

# test 6: Already built	
#   inputs: yes, 5, 4, 4, 10, 1000, 10

# test 7:All at once
#   inputs: yes, 0, 0, 0, 3, 3000, 12

# test 7:house and hotel
#   inputs: yes, 3, 3, 3, 1, 5000, 3