# if statements checking

alien_color = ['green','yellow','red']

if 'violet' in alien_color :
    print("player is just earned 5 points")
else:
    print()

alien_color = ['green','yellow','red']
alien = input("please enter the color :")
if alien in alien_color:
    print("player just earned 5 points")
elif alien in alien_color:
    print("player just earned 10 points")
else:
    print("playeer has just earned 15 points")


#stage of life

age = int(input("please enter your age :"))

if age < 2:
    print("Person is Baby")
elif age >= 2 and age < 4:
    print("Person is Toddler")
elif age >= 4 and age < 13:
    print("Person is Kid")
elif age >= 13 and age < 20:
    print("Person is Toddler")
elif age >= 20 and age < 65:
    print("Person is Adult")
else:
    print("Person is Elder")


#loopin through the list

users = ['ram','ganesh','somesh','admin','suresh','admin']

if users:
    for user in users:
        if user == "ADMIN":
            print("Hello Admin,would you like to see a status of report ?")
        else:
            print(f"Hello {user.title()}, thank you for logging again")
else:
    print("We need to fine some Users!")

#unique username

current_users = ['John','Michael','Rob','Jessica','Mitchelle']

new_users = ['Rebecca','Jaquelin','JOHN','Julia','ROB']

for new_user in new_users:
    if new_user.title()  in current_users:
         print("User name is availabel")
    else:
        print("Enter new user name")

