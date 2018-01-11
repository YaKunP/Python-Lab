# Create a deck of cards
deck = [x for x in range(52)]    # deck = list(range(52))

# Create suits and ranks lists
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]     # 黑桃 红桃 方块 梅花
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

# Shuffle the cards
import random
random.shuffle(deck)

# Display the first four cards
for i in range(4):
    suit = suits[deck[i] // 13]
    rank = ranks[deck[i] % 13]
    print("Card number", deck[i], "is the", rank, "of", suit)
