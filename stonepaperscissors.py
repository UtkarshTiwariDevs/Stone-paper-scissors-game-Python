import random

str = ["st", "p", "sc"]
comp_choice = random.choice(str)
# print(choice)
comp_points = 0
user_points = 0
max_points = int(input("Enter max no. of points"))
played = 0
while played < max_points:
    user_choice = input("Enter st , p , sc for stone , paper and scissors recpectively ")

    if user_choice == "st" and comp_choice == "st":
        played += 1
    elif user_choice == "st" and comp_choice == "p":
        comp_points += 1
        played += 1
    elif user_choice == "st" and comp_choice == "sc":
        user_points += 1
        played += 1

    elif user_choice == "p" and comp_choice == "st":
        user_points += 1
        played += 1
    elif user_choice == "p" and comp_choice == "p":
        played += 1
    elif user_choice == "p" and comp_choice == "sc":
        comp_points += 1
        played += 1

    elif user_choice == "sc" and comp_choice == "st":
        comp_points += 1
        played += 1
    elif user_choice == "sc" and comp_choice == "p":
        user_points += 1
        played += 1
    elif user_choice == "sc" and comp_choice == "sc":
        played += 1
    else:
        print("wrong choice entered")

    if played == max_points and user_points > comp_points:
        print(f"You win with points {user_points} and computer points {comp_points}")
    elif played == max_points and user_points == comp_points:
        print(f"You tie with points {user_points} and computer points {comp_points}")
    elif played == max_points and user_points < comp_points:
        print(f"You loose with points {user_points} and computer points {comp_points}")
    else:
        continue