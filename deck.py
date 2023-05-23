from __future__ import annotations

from cards import Card

class Deck:
    # private attribute
    __suits: list[str] = ["hearts", "diamonds", "spades", "clubs"]

    # Constructor
    def __init__(self) -> None:
        self.deck: list[Card] = []

        for suit in range(4):
            for nb in range(1, 14):
                c = Card(nb, self.__suits[suit])
                self.deck.append(c)

    # Default functions
    def __str__(self) -> str:
        return f"{self.deck}"
    
    def __len__(self) -> int:
        return len(self.deck)

    # Public functions
    def fuse(self, d: Deck) -> None:
        self.deck += d.deck

    def shuffle(self) -> None:
        from random import shuffle
        shuffle(self.deck)

    def pick(self, index: int = ...) -> Card:
        self.shuffle()
        if type(index) != int:
            return self.deck.pop(0)
        return self.deck.pop(index)
    
if __name__ == "__main__":
    d = Deck()

    for i in range(5):
        print(d.pick())
    print(d)
    print(len(d))