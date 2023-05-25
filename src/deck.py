from __future__ import annotations
from random import shuffle

from cards import Card

class Deck:
    """Deck of 52 cards (4 suits of 13 cards)

    Attributes:
        deck (list[Card]): A deck of 52 cards
    """

    # private attribute
    __suits: list[str] = ["hearts", "diamonds", "spades", "clubs"]

    # Constructor
    def __init__(self) -> None:
        self.deck: list[Card] = []

        for suit in range(4):
            for nb in range(1, 14):
                c = Card(nb, self.__suits[suit])
                self.deck.append(c)

    # Default methods
    def __str__(self) -> str:
        """Return the deck as a string

        Returns:
            str: the deck as a string
        """
        return f"{self.deck}"
    
    def __len__(self) -> int:
        """Return the number of cards in the deck

        Returns:
            int: number of cards in the deck
        """
        return len(self.deck)

    # Verification method
    def isEmpty(self) -> bool:
        """Return True if the deck is empty

        Returns:
            bool: True if the deck is empty, False otherwise
        """
        return (len(self) == 0)

    # Public methods
    def fuse(self, d: Deck) -> None:
        """Fuse two decks together

        Args:
            d (Deck): deck to fuse with
        """
        self.deck += d.deck

    def shuffle(self) -> None:
        """Shuffle the deck
        """
        shuffle(self.deck)

    def pick(self, index: int = ...) -> Card:
        """Pick a card from the deck

        Args:
            index (int, optional): index of the card to pick. First card by default.

        Returns:
            Card: the card picked 
        """
        self.shuffle()
        if type(index) != int:
            return self.deck.pop(0)
        return self.deck.pop(index)
    
    def draw(self) -> Card:
        """Draw the first card of the deck

        The deck is shuffled each time a card is drawn.

        Returns:
            Card: the first card of the deck
        """
        return self.pick()

    def reset(self) -> None:
        """Reset the deck
        """
        self.__init__()

if __name__ == "__main__":
    d = Deck()

    for i in range(5):
        print(d.pick())

    print(d)
    print(len(d))