import random
random_number=random.randint(1,100)
count = 0
while(True):
    count += 1
    user_input=int(input("Guess the number between 1 and 100:\n"))
    if(user_input < random_number):
        print("Too low")
    elif(user_input>random_number):
        print("Too high")
    else:
        print("Correct! You guessed the number in ",count," attempts")
        break;
