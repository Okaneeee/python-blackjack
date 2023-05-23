from __future__ import annotations

class Game:
    """Game of blackjack

       Blackjack rules:
            - 1 deck of 52 cards
            - 2 cards for the player
            - 2 cards for the dealer (1 hidden)
            - Player can:
                - Hit (draw a card)
                - Stand (end the draw phase)
                - Double (draw a card and double the bet)
                - Split (split the hand in two if the two cards are of the value of 10) 
                - Insurance (if dealer might has blackjack)   

            - Dealer must hit if his score is less than 17
            - Dealer must stand if his score is more than 17

            - If player has blackjack (21), he wins 1.5x his bet
            - If player has more than the dealer, he wins his bet
            - If player has the same score as the dealer, he gets his bet back
            - If player has more than 21, he loses his bet
            - If player has less than the dealer, he loses his bet
    """
    def __init__(self) -> None:
        pass

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

    def bet(self, value: int) -> None:
        """
        """
        ...

    def deal(self) -> bool:
        """
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
        return True if ... else False
    
if __name__  == "__main__":
    pass