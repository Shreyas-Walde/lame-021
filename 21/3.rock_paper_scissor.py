import random

user_wins = 0
computer_wins = 0

options = ["R","P","S"]

while True:
    user_input = input("Type R/P/S or q: ").upper()
    if user_input == 'Q':
        break

    if user_input not in options:
        print("Enter valid input: ")
        continue

    random_number = random.randint(0,2)
    # 0 -> R, 1 -> P, 2 -> S
    computer_pick = options[random_number]
    print("Computer chooses",computer_pick + ".")

    if user_input == "R" and computer_pick == "S":
        print("Won!")
        user_wins+=1
        continue

    elif user_input == "P" and computer_pick == "R":
        print("Won!")
        user_wins+=1
         

    elif user_input == "S" and computer_pick == "P":
        print("Won!")
        user_wins+=1
    
    else:
        print("You lost!")
        computer_wins +=1
        

print("You won", user_wins)
print("Computer won", computer_wins)
print("Goodbye")


