"""
Blackjack rules:
    - 1 deck of 52 cards
    - 2 cards for the player
    - 2 cards for the dealer (1 hidden)
    - Player can:
        - Hit (draw a card)
        - Stand (end the draw phase)
        - Double (draw a card and double the bet)
        - Split (split the hand in two if the two cards are of the value of 10) 
        - Insurance (only if dealer might has blackjack (ace as first card))   

    - Dealer must hit if his score is less than 17
    - Dealer must stand if his score is more than 17

    - If player has blackjack (21), he wins 3x his bet
    - If player has more than the dealer, he wins 2x his bet
    - If player wins insurance, he wins 2.5x his bet
    - If player has the same score as the dealer, he gets his bet back
    - If player has more than 21, he loses his bet
    - If player has less than the dealer, he loses his bet

    - Blackjack only occur with the first two cards
"""
from __future__ import annotations

from deck import Deck
from player import Player, Dealer


class Game:
    """Game of blackjack

    Args:
        player (Player): The player
        dealer (Dealer): The dealer (Optional, defaults to Dealer)
    
    Attributes:
        player (Player): The player
        dealer (Dealer): The dealer
        deck (Deck): The deck

    Methods:
        bet() -> None: Bet money
        deal() -> bool: Deal cards
        split() -> list[Game]: Split the game in two
        double() -> bool: Double the bet and draw a card
        hit() -> bool: Draw a card
        stand() -> bool: End the draw phase
        insurance() -> bool: Check if dealer has blackjack
    """
    # Constructor
    def __init__(self, player: Player, dealer: Dealer = Dealer()) -> None:
        self.player: Player = player
        self.dealer: Dealer = dealer
        self.deck: Deck = Deck()

    # Default methods
    def __str__(self) -> str:
        """Returns the game as a string

        Returns:
            str: the game as a string
        """
        return f"{self.player}\n{self.dealer}"

    # Public methods

    # Before game methods
    def bet(self) -> None:
        """
        """
        toBet = int(input("How much do you want to bet?\n"))
        self.player.setBet(toBet)

    def deal(self) -> bool:
        """
        """
        act = input("Did you finish your bet? (Y/N)\n")
        while act != "Y" and act != "N":
            act = input("Did you finish your bet? (Y/N)\n")
        if act == "N":
            return False
        return True

    # In-Game methods
    def split(self) -> list[Game]:
        """
        To verify: 
            - saved money >= betted money
            - card 1 & 2 = 10 each (20 total)
        To return:
            - Game 1 with right card (wait until Standing)
            - Game 2 with left card (wait unti Standing)
        Results:
            - if game1.score > dealer.score: betted*2
            - if game2.score > dealer.score: betted*2
            - if game1.score & game2.score > dealer.score: betted*4
            - if gameX.score = dealder.score: betted = betted
            - else (lose) betted = 0
        """
        ...

    def double(self) -> bool:
        """
        Return true when called
        """
        # TODO: draw a card and add it to player hand
        return True

    def hit(self) -> bool: 
        """
        To verify:
            - game.value > 21 ? true : false
        """
        ...

    def stand(self) -> bool:
        """
        Return true when called
        (Basically end the draw phase)
        """
        return True

    def insurance(self) -> bool:
        """Check if dealer has blackjack
        Can only be called if dealer has an ace as first card

        Returns:
            bool: True if he has, else False
        """
        """
        To verify:
            - saved money >= betted money / 2
        Results:
            - Dealer has blackjack
            - Dealer doens't have blackjack
        """
        return True if ... else False

    # Main method
    def play(self) -> None:
        """
        """
        ...

if __name__  == "__main__":
    g = Game(Player("J1"))
    print(g)