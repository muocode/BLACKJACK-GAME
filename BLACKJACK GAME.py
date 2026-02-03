import random
from art import blackjack


def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare_score(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "You lose"
    elif u_score == 0:
        return "You win"
    elif u_score > 21:
        return "You lose!"
    elif c_score > 21:
        return "The computer went over. You win"
    elif u_score > c_score:
        return "You win!"
    elif c_score > u_score:
        return "You lose!"
    else:
        return "Error: Unexpected case!"


def play_game():
    print(blackjack)
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    players_turn_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not players_turn_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"User's cards are: {user_cards}, user's current score: {user_score}")
        print(f"Computer's cards: {computer_cards [:len(user_cards)-1]}")

        if user_score == 0 or computer_score == 0 or user_score >= 21 or computer_score >= 21:
            players_turn_over = True
        else:
            user_should_deal = input("type 'y' for a hit or 'n' to pass \n").lower()
            if user_should_deal in ['y', 'yes']:
                    user_cards.append(deal_card())
            elif user_should_deal in['n', 'no']:
                    players_turn_over = True
            else:
                    print("You entered an invalid answer. Please type 'y' or 'n'")

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"user final hand: {user_cards}, user score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, computer's score: {computer_score}")
    print(compare_score(user_score, computer_score))

while input("Do you want to play a game of BlackJack? \n").lower() in ['y', 'yes']:
    print("\n" * 30)
    play_game()

print("Okay, what game would you prefer?")



































