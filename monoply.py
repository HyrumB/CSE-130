
def main():
    own_green_bool = is_green_owned()
    tokens_on_PA_ave = whats_on_pensylvania_ave()
    tokens_on_CA_ave = whats_on_carolina_ave(tokens_on_PA_ave)
    tokens_on_PC_ave = whats_on_pacific_ave(tokens_on_PA_ave)


def is_green_owned():
    own_all_green_inpt = input("Do you own all the green properties? (y/n) ")
    own_all_green_bool = False

    if own_all_green_inpt == "y":
        own_all_green_bool = True
        return own_all_green_bool
    else:
        print("\n You cannot purchase a hotel until you own")
        print("all the properties of a given color group.")
        return own_all_green_bool

def whats_on_pensylvania_ave():
    tokens_on_PA_ave = input("What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel) ")
    tokens_on_PA_ave = int(tokens_on_PA_ave)

    if tokens_on_PA_ave == 5:
        print("\n You cannot purchase a hotel if the property already has one.")
        return tokens_on_PA_ave
    
    else:
        return tokens_on_PA_ave

def whats_on_carolina_ave(tokens_on_PA):
    tokens_on_CA_ave = input("What is on Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel) ")
    tokens_on_CA_ave = int(tokens_on_CA_ave)

    if tokens_on_CA_ave == 5 and tokens_on_PA == 4:
        print("\n Swap North Carolina's hotel with Pennsylvania's 4 houses..")

    else:
        return tokens_on_CA_ave
        
def whats_on_pacific_ave(tokens_on_PA):
    tokens_on_PC_ave = input("What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel) ")
    tokens_on_PC_ave = int(tokens_on_PC_ave)

    if tokens_on_PC_ave == 5 and tokens_on_PA == 4:
        print("\n Swap North Carolina's hotel with Pennsylvania's 4 houses..")

    else:
        return tokens_on_PC_ave




main()