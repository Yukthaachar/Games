# rock=0, paper=1, scissor=2
Rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissor="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
def player1():
    import random
    ascii_images=[Rock,Paper,Scissor]
    user = int(input("WHAT DO YOU CHOOSE? (Type 0 for rock, 1 for paper, 2 for scissor):\n"))
    if user in range(0,3):
        print(ascii_images[user])

    computer = random.randint(0,2)
    print(f"COMPUTER'S CHOICE: \n{ascii_images[computer]}")

    if user >=3 or user <0:
        print("INVALID INPUT, YOU LOSE!")
    elif user ==0 and computer == 2:
        print('YOU WIN!')
    elif user==2 and computer == 0:
        print('YOU LOSE!')
    elif user>computer:
        print('YOU WIN!')
    elif computer>user:
        print('YOU LOSE!')
    elif user ==computer:
        print("GAME IS DRAW!")


def player2():
    ascii_images = [Rock, Paper, Scissor]
    user1 = int(input("WHAT DO PLAYER1 CHOOSE? (Type 0 for rock, 1 for paper, 2 for scissor):\n"))
    if user1 in range(0, 3):
        print(ascii_images[user1])

    user2 = int(input("WHAT DO PLAYER2 CHOOSE? (Type 0 for rock, 1 for paper, 2 for scissor):\n"))
    if user2 in range(0, 3):
        print(ascii_images[user2])

    if user1 >= 3 or user1 < 0:
        print("INVALID INPUT, PLAYER1 LOSE!")
    elif user2 >= 3 or user2 < 0:
        print("INVALID INPUT, PLAYER2 LOSE!")
    elif user1 == 0 and user2 == 2:
        print('PLAYER1 WIN!')
    elif user1 == 2 and user2 == 0:
        print('PLAYER2 WIN!')
    elif user1 > user2:
        print('PLAYER1 WIN!')
    elif user2 > user1:
        print('PLAYER2 WIN!')
    elif user1 == user2:
        print("GAME IS DRAW!")


choose = int(input("HOW DO YOU WANT TO PLAY?\n TO PLAY WITH COMPUTER PRESS 1\n TO PLAY WITH TWO PLAYERS PRESS 2\n"))
if choose >= 3 or choose <= 0:
    print("INVALID CHOICE")
elif choose == 1:
    player1()
elif choose == 2:
    player2()


