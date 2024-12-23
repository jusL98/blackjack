from carddeck import deck
import random

# Player Class
class Player:
    def __init__(self):
        self.card1 = random.randint(0,51)
        self.card2 = random.randint(0,51)
        
        self.card1_name = f'{deck[self.card1].rank} of {deck[self.card1].suit}'
        self.card2_name = f'{deck[self.card2].rank} of {deck[self.card2].suit}'
        
        self.card1_value = deck[self.card1].card_value()
        self.card2_value = deck[self.card2].card_value()
        self.total_value = self.card1_value + self.card2_value

        self.new_cards_name_list = []
        self.new_cards_value_list = []
    
    # New Card On Hit
    def hit(self):
        self.new_card = random.randint(0,51)
        self.new_card_name = f'{deck[self.new_card].rank} of {deck[self.new_card].suit}'
        self.new_card_value = deck[self.new_card].card_value()

        self.new_cards_name_list.append(self.new_card_name)
        self.new_cards_value_list.append(self.new_card_value)

        self.total_value += self.new_card_value

def main():
    # Prints initial card deal for testing purposes.
    player = Player()
    print(f'Player Cards: {player.card1_name}, {player.card2_name}')
    print(f'Player Card Values: {player.card1_value}, {player.card2_value}')
    print(f'Player Total Value: {player.total_value}')

    print()

    dealer = Player()
    print(f'Dealer Cards: ????, {dealer.card2_name}')
    print(f'Dealer Card Values: ????')
    print(f'Dealer Total Value: ????')

if __name__ == '__main__':
    main()