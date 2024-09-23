import random

# يعرف مجموعة البطاقات
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# ينشئ المجموعة الكاملة من البطاقات
deck = []
for suit in suits:
    for rank in ranks:
        deck.append(f'{rank} of {suit}')

# يخلط البطاقات
random.shuffle(deck)

# توزيع البطاقات على اللاعبين
player1_deck = deck[:26]
player2_deck = deck[26:]

# تنفيذ اللعبة
rounds = 0
while player1_deck and player2_deck and rounds < 1000:
    card1 = player1_deck.pop(0)
    card2 = player2_deck.pop(0)
    
    print(f'Player 1: {card1} - Player 2: {card2}')
    
    if ranks.index(card1.split()[0]) > ranks.index(card2.split()[0]):
        player1_deck.extend([card1, card2])
    elif ranks.index(card1.split()[0]) < ranks.index(card2.split()[0]):
        player2_deck.extend([card1, card2])
    else:
        war_cards = [card1, card2]
        while True:
            if len(player1_deck) < 3 or len(player2_deck) < 3:
                break
                
            for _ in range(3):
                war_cards.append(player1_deck.pop(0))
                war_cards.append(player2_deck.pop(0))
            
            last_card1 = war_cards[-2]
            last_card2 = war_cards[-1]
            
            print(f'War! Player 1: {last_card1} - Player 2: {last_card2}')
            
            if ranks.index(last_card1.split()[0]) > ranks.index(last_card2.split()[0]):
                player1_deck.extend(war_cards)
                break
            elif ranks.index(last_card1.split()[0]) < ranks.index(last_card2.split()[0]):
                player2_deck.extend(war_cards)
                break

    rounds += 1

# إعلان الفائز
if len(player1_deck) > len(player2_deck):
    print('Player 1 wins!')
elif len(player1_deck) < len(player2_deck):
    print('Player 2 wins!')
else:
    print('Its a tie!')
