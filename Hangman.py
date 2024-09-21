stages=['''
  +----------+
  |          |
  ()         |
/ | \        |
 / \         |
             |
             |
 ===============
 ''', '''
  +----------+
  |          |
  ()         |
/ | \        |
 /           |
             |
             |
 ===============
 ''','''
  +----------+
  |          |
  ()         |
/ | \        |
             |
             |
             |
 ===============
 ''','''
  +----------+
  |          |
  ()         |
/ |          |
             |
             |
             |
 ===============
 ''','''
  +----------+
  |          |
  ()         |
  |          |
             |
             |
             |
 ===============
 ''','''
  +----------+
  |          |
  ()         |
             |
             |
             |
             |
 ===============
 ''','''
  +----------+
  |          |
             |
             |
             |
             |
             |
 ===============
 ''','''
  +----------+
             |
             |
             |
             |
             |
             |
 ===============
 '''
]

import random
user_input = ""
options=["ANIMAL","FRUIT","HOUSEHOLD ITEMS","VEGETABLE"]
context={
    "ANIMAL":['cat','dog','frog','cow','elephant','zebra','snake','donkey','squirrel','cheetah','rabbit','horse'],
    "FRUIT":['apple','orange','grapes','strawberry','banana','cherry','watermelon','peach','pomegranate','date','rambutan'],
    "VEGETABLE":['tomato', 'onion', 'potato', 'pumpkin', 'broccoli', 'brinjal', 'garlic', 'cucumber', 'coriander', 'spinach', 'pea'],
    "HOUSEHOLD ITEMS":['fan', 'bulb', 'bucket', 'clock', 'desk', 'carpet', 'pillow', 'almirah', 'broom', 'chair', 'blender', 'cloth'],
}

player_lives=7
word_list = random.choice(options)
print("GUESS THE ",word_list)
chosen_word=random.choice(context[word_list])
word_length = len(chosen_word)

blanks=''
for letter in range(word_length):
    blanks += '_'
print(blanks)

gameOver = False
correct_alphabets=[]

while not gameOver:
    guess = input("\nGuess the original word: ").lower()
    display = ''

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_alphabets.append(letter)
        elif letter in correct_alphabets:
            display += letter
        else:
            display +='_'
    print(display)

    if guess not in chosen_word:
        player_lives -= 1
        if player_lives == 0:
            gameOver = True
            print("You lose")

    if "_" not in display:
        gameOver = True
        print("You Win")

    print(stages[player_lives])