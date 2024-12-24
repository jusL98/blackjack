from playerdealer import Player
import time


# Game Start
print('****************************************')
print(f'{"Welcome to Blackjack!" :^40}')
print('****************************************')
print()

while True:
    play = input('Would you like to play? (Y/N): ').upper()
    if play == 'Y':
        break
    elif play == 'N':
        print('Exiting Game...')
        exit()
    else:
        print('Invalid entry.')

# Initial Card Deal
print('Dealing cards...\n\n')
time.sleep(1.5)

dealer = Player()
print(f'Dealer Cards: {"????"}, {dealer.card2_name}')
print(f'Dealer Total Value: ???? (>{dealer.card2_value})')
print('----------------------------------------')
player = Player()
print(f'Player Cards: {player.card1_name}, {player.card2_name}')
print(f'Player Total Value: {player.total_value}')
print()


# Handle Hit/Stand
while True:
    print()
    hit_stand = input('Hit or Stand? (H/S): ').upper()

    # Hit
    if hit_stand == 'H':
        player.hit()
        print(f'Dealer Cards: {"????"}, {dealer.card2_name}')
        print(f'Dealer Total Value: ???? (>{dealer.card2_value})')
        print('----------------------------------------')
        print(f'Player Cards: {player.card1_name}, {player.card2_name}, {", ".join(player.new_cards_name_list)}')
        print(f'Player Total Value: {player.total_value}')

        print()
        if player.total_value < 21:
            continue
        elif player.total_value > 21:
            print()
            print('****************************************')
            print('Sorry, YOU LOSE!')
            print(f'You were over 21.')
            break
        elif player.total_value == 21:
            print()
            print('****************************************')
            print('Congratulations, YOU WIN!')
            print(f'You reached 21.')
            break

    # Stand
    elif hit_stand == "S":      
        print()  
        if player.total_value > dealer.total_value:
            print()
            print('****************************************')
            print('Congratulations, YOU WIN!') 
            print('You were closer to 21 than the dealer.') 
        elif player.total_value < dealer.total_value:
            print()
            print('****************************************')
            print('Sorry, YOU LOSE!')
            print('The dealer was closer to 21.')
        elif player.total_value == dealer.total_value:
            print()
            print('****************************************')
            print('TIE!')
            print('You and the dealer had the same total value.')
        break

    # Hit/Stand Invalid Entry 
    else:
        print('Invalid entry.')

print(f'- Player Total Value: {player.total_value}')
print(f'- Dealer Total Value: {dealer.total_value}')
print('****************************************')


# Scenarios To Resolve
# - What if player gets 21 in first two cards ... note - not an issue as not currently possible because ace is only worth 1
# - What if dealer gets 21 in first two cards ... note - not an issue as not currently possible because ace is only worth 1