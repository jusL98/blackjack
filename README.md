<a id="readme-top"></a>

# Blackjack
This game is a terminal blackjack game that I created to learn OOP in python. The game features randomized card dealing, intuitive prompts for the user and information about the total value of both the player and dealer's hand.

<p align="left">
   <img width="600" alt="image" src=""/>
</p>

## Description
Blackjack involves a computer dealer and 1 player. The goal of this popular card game is for the player to achieve a hand closer to 21 than the dealer without busting. The game features a clean terminal user interface, intuitive prompting, invalid entry handling and the standard blackjack gameplay. 

In this modified version for simplicity:
- There is no betting
- Ace is only worth 1 point (not 1 or 11 sometimes)
- Cards may sometimes duplicate
- The dealer does not hit after you stand

## Built With
- [Python 3.13](https://www.python.org/): Description

## Quick Start
### Prerequisites
- OS
- Language Version or higher
- Terminal or CLI Access

### Installation
To install the Blackjack Game, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/jusL98/blackjack-game.git
   cd blackjack-game
   ```

2. Ensure that you have python running on your system.

### Setup
N/A

### Run
3. Run the Blackjack Game.
   ```bash
   python main.py
   ```

## Usage
1. To play, input "Y" when prompted or "N" to quit the game.
2. 2 cards will be dealt for the dealer & 2 cards will be dealt for you when the game begins.
3. Only 1 of the dealer's 2 cards will be displayed to you.
4. Your total card value is displayed to the you but the dealer's total card value is hidden. 
5. Input "H" for hit to receive another card if you think you currently have less card value than the dealer and if you can advance closer to 21 without busting.
6. Continue hitting if you think you can advance closer to 21 without busting.
7. Otherwise, input "S" for stand to stay with your cards if you think you are closer to 21 than the dealer.
8. If you hit 21, bust or choose stand, the game will calculate if you win, lose or tie against the dealer, whichever comes first.

## Contributing
1. Fork & branch off main.
2. Make your changes.
3. PRs welcome!

## Project Structure
```
├── blackjack/
│   ├── carddeck.py                    # contains a class definition for a card and function to create a deck of 52 cards
│   ├── playerdealer.py                # contains a class definition to create a player (player or dealer)
│   └── main.py                        # contains the main game logic and gameplay flow
```

## Acknowledgements
This project was created to learn object oriented programming for Python.

## License
This project is licensed under the [MIT](LICENSE.txt) License. See LICENSE.txt for more information.

<br>

---

<br>
Thank you!