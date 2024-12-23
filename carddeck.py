# Setup Cards: Ranks, Suits, Card Values
ranks = ['ACE','2','3','4','5','6','7','8','9','10','JACK','QUEEN','KING']
suits = ['HEARTS','DIAMONDS','SPADES','CLUBS']
card_values = {
    'ACE': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'JACK': 10,
    'QUEEN': 10,
    'KING': 10
}

# Card Class
class Card:
    num_cards = 0

    def __init__(self, rank, suit):
        self.rank = rank.upper() # Ace, 2, 3, 4, 5, 6, 7, 8, 9, Jack, Queen, King
        self.suit = suit.upper() # Hearts, Diamonds, Spades, Clubs
        Card.num_cards += 1

    def card_value(self):        
        return card_values.get(self.rank)
            
# Create Deck Of Cards Using Card Class
def create_deck():
    deck = []
    for i in range(4):
        for j in range(13):
            new_card = Card(ranks[j],suits[i])
            deck.append(new_card)
            #print(f'{new_card.rank} of {new_card.suit}') 
        #print('------------')
    #print(Card.num_cards)
    return deck

deck = create_deck()

def main():
    # Prints the value of 1 card under temp's index for testing purposes.
    temp = 0
    print(f'{deck[temp].rank} of {deck[temp].suit}')
    print(deck[temp].card_value())

if __name__ == '__main__':
    main()