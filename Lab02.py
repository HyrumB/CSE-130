import json

# Cracks open the Json file.
java_file = open(r"C:\Users\hyrum\Documents\collage\code_4_collage\CSE 130\Lab02.json")

#print(file.read()) 

username_list = []
password_list = []
  
# # This iterating through the json list
for i in java_file:

    if "username" in i:
        pass_or_user = True

    elif "password" in i:
        pass_or_user = False
    
    # this puts the value of i into a list if it contains the character (") 
    # and the boolien pass_or_user is in the user position (true)  
    elif "\"" in i and pass_or_user:
        username_list.append(i.strip(",\n ,'") )

    # this puts the value of i into a list if it contains the character (") 
    # and the boolien pass_or_user is in the password position (false)  
    elif "\"" in i and not pass_or_user:
        password_list.append(i.strip(",\n ,'") )


print(f"\nusername:\n {username_list}")

print(f"\npasswords:\n {password_list}")
        