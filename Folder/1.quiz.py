print("Welcome to Computer Quiz")

playing = input("Wanna play? ")

if playing.lower() != "yes":
    quit()

print("Let's play!")

score = 0
answer = input("What's CPU ").lower()
if answer == "cpu":
    print("correct!")
    score+=1
else: 
    print("Nope")

answer = input("What's GPU ").lower()
if answer == "gpu":
    print("correct!")
    score+=1
else: 
    print("Nope")

answer = input("What's japan ").lower()
if answer == "japan":
    print("correct!")
    score+=1
else: 
    print("Nope")

print("you got " + str(score) + " question correct")