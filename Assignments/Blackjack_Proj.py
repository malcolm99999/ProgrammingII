"""
I want to make a project that is blackjack against the computer, Over the break I will create a UI for it
"""

import random

deck = 4* [2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "ace"]
player_hand = []
dealer_hand = []
def draw_card(hand):
    card = random.choice(deck)
    if card == "jack" or card == "queen" or card == "king":
        hand.append(10)
    elif card == "ace":
        hand.append(11)
    else:
        hand.append(card)
def deal():
    draw_card(dealer_hand)
    draw_card(dealer_hand)
    draw_card(player_hand)
    draw_card(player_hand)
def stay(hand):
    print("Dealer is sitting at " + str(sum(dealer_hand)))
def hit(hand):
    new_card = draw_card(hand)
def determine_winner(player_hand, dealer_hand):
    if sum(player_hand) and sum(dealer_hand) <= 21:
        if sum(player_hand) > sum(dealer_hand):
            print("you win!")
        elif sum(dealer_hand) > sum(player_hand):
            print("dealer won :(")
        elif sum(dealer_hand) == sum(player_hand):
            print("dealer won :(")
    elif sum(player_hand) > 21:
        print("bust, you lose")
    elif sum(dealer_hand) > 21:
        print("dealer bust")
    elif sum(dealer_hand) > 21 and sum(player_hand) > 21:
        print("Bust, but dealer busted also")




#def hit_or_stay():
def dealer_rules():
    if sum(dealer_hand) <= 17:
        hit(dealer_hand)
        print("Dealer hits")
        print("Dealer now has: " + int(sum(dealer_hand)))
    if sum(dealer_hand) >= 18:
        stay(dealer_hand)#


print(" ")
print("                     welcome to blackjack, here are some rules before you begin")
print(" ")
print("1. 21 wins it")
print("2. You can either hit or stay")
print("3. Dealer stays at soft 18")
print("4. 3 limit to hits")
print(" ")
print("ready?")
start = input("")
if start.lower() == "yes":
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    deal()
    print("You were dealt: "  + str(min(player_hand)) + (" and ") + str(max(player_hand)))
    print(" ")
    playerq = input("would you like to hit or stay: ")
    if playerq.lower() == "stay":
        stay(player_hand)
        print("You are staying at soft " + str(sum(player_hand)))
    elif playerq.lower() == "hit":
        hit(player_hand)
        print("You Hit")
        sum_num = str(sum(player_hand))

        print("You now have " + sum_num)

    print("\n\n ")
    print("Dealer was dealt: " + str(min(dealer_hand)) + (" and ") + str(max(dealer_hand)))
    determine_winner(player_hand, dealer_hand)




"""

def win_conditions(player_hand, dealer_hand):
    if
"""
