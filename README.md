# Blackjack Game
This is a modified blackjack game which is my first major project to practice using object oriented programming.

## About This Project
The blackjack game runs in the terminal with a computer dealer and 1 player. The goal of this familiar card game is for the player to get a hand closer to 21 than the dealer without going over (busting). View more instructions in [Usage](#Usage).

## Technologies Used
Python 3.13

## Installation
To install the Blackjack Game, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/jusL98/blackjack-game.git
   cd blackjack-game
   ```

2. Ensure that you have python running on your system.

3. Install the required dependencies:

   ```bash
   N/A
   ```

4. Run the Blackjack Game.
   ```bash
   python main.py
   ```

## Usage
1. To play, input "Y" when prompted.
2. Two cards will be dealt for the dealer & two cards will be dealt for you (the player) when the game starts.
3. Only 1 of the dealer's 2 cards will be displayed to you.
4. Your total card value is displayed to the you but the dealer's total card value is hidden. 
5. Input "H" for hit to receive another card if you think you currently have less card value than the dealer and if you can advance closer to 21 without busting.
6. Continue hitting if you think you can advance closer to 21 without busting.
7. Otherwise, input "S" for stand to settle with your cards if you think you are closer to 21 than the dealer.
8. If you hit 21, bust or choose stand, the game will calculate if you win, lose or tie against the dealer, whichever comes first.
9. Have fun!

## Modifications Compared To Traditional Blackjack (for simplicity sake and my lack of current expertise to do so)
- No betting
- Ace is only worth 1 (not 11 as well)
- Cards may sometimes duplicate
- Dealer does not hit after you stand

## Future Improvements/Updates (mostly to address the modifications above)
- Betting
- Ace being worth 1 or 11
- Resolve duplication of cards
- Dealer hitting after stand
- Multiple players
- "Splitting Pairs"
- "Doubling Down"

---

Thank you!
