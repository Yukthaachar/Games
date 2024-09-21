import random
# Constants
user_input=""
max_attempt = 3
options=["ANIMAL","FRUIT","VEGETABLE","HOUSEHOLD ITEMS"]
context={
    "ANIMAL":['cat','dog','frog','cow','elephant','zebra','snake','donkey','squirrel','cheetah','rabbit','horse'],
    "FRUIT":['apple','orange','grapes','strawberry','banana','cherry','watermelon','peach','pomegranate','date','rambutan'],
    "VEGETABLE": ['tomato', 'onion', 'potato', 'pumpkin', 'broccoli', 'brinjal', 'garlic', 'cucumber', 'coriander', 'spinach', 'pea'],
    "HOUSEHOLD ITEMS": ['fan', 'bulb', 'bucket', 'clock', 'desk', 'carpet', 'pillow', 'almirah', 'broom', 'chair', 'blender', 'cloth'],
}

word_list = random.choice(options)
chosen_word=random.choice(context[word_list])
word = list(chosen_word)
random.shuffle(word)
scrambled_word = ''.join(word)
# Introduction
print("Welcome to the Word Scramble Game!\n")
print("Guess the word related to ",word_list,'\n')
print("Your scrambled word is: ",scrambled_word)
# Main Game Loop
while max_attempt > 0:
    user_input = input("\nGuess the original word: ").lower()
    if user_input == chosen_word:
        print("\nCongratulations! You gave the correct answer!!!")
        print("THE PLAYER WINS!")
        break
    else:
        max_attempt -= 1
        # If out of attempts
        if max_attempt == 0 and chosen_word != user_input:
            print("\nYou are out of chances.")
            print("The correct word was: ", chosen_word, ".")
            print("Better luck next time!")
        else:
            print("\nIncorrect! Try again. You have ", max_attempt, " attempt(s) left.")

