from __future__ import annotations

class Game:
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
        """
        Check if dealer has blackjack
        True if he has, else False
        """
        return True if ... else False
    
if __name__  == "__main__":
    def a(index):
        deck = [1, 2, 3]
        try:
            return deck.pop(index)
        except IndexError:
            return deck.pop(-1)
    
    print(a(1))