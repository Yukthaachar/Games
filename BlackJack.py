import random
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_scores(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Both got the same number, so the game is a draw."
    elif computer_score == 0:
        return "Computer got a perfect score, so player loses."
    elif user_score == 0:
        return "You got the perfect score, so player wins."
    elif user_score > 21:
        return "Player got a number more than 21, so computer wins."
    elif computer_score > 21:
        return "Computer score exceeds 21, so player wins."
    elif user_score > computer_score:
        return "Player wins!"
    else:
        return "Computer wins!"

# Initialize cards
# user_cards = [deal_card() for _ in range(2)]
# computer_cards = [deal_card() for _ in range(2)]
user_cards = []
computer_cards = []
for fillingcards in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

game_over = False
while not game_over:
    user_score = calculate_scores(user_cards)
    computer_score = calculate_scores(computer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 0 or user_score > 21:
        game_over = True
    else:
        user_should_deal = input("Type 'y' to get another card, or 'n' to pass:\n")
        if user_should_deal == 'y':
            user_cards.append(deal_card())
        else:
            game_over = True

# Computer's turn
while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_scores(computer_cards)

print(f"Your final hand: {user_cards}, final score: {user_score}")
print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
print(compare(user_score, computer_score))