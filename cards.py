from __future__ import annotations

# hearts ♥ - diamonds ♦ - spades ♠ - clubs ♣

class Card:
    # Constructor
    def __init__(self, number: int, suit: str) -> None:
        self.number: int = number
        self.suit: str = suit
        self.value: int = self.__cardValue()

    # Default functions
    def __repr__(self) -> str:
        return f"{self.__numberFormat()}{self.__suitFormat()}"
    
    def __str__(self) -> str:
        return self.__repr__()

    def __len__(self) -> int:
        return len(self.__str__())

    # Private functions
    def __numberFormat(self) -> str:
        match self.number:
            case 1:
                return "A"
            case 11:
                return "J"
            case 12:
                return "Q"
            case 13:
                return "K"
            case _:
                return str(self.number)

    def __suitFormat(self) -> str:
        self.suit += 's' if self.suit[-1] != 's' else ""

        match self.suit:
            case "hearts":
                return "♥"
            case "diamonds":
                return "♦"
            case "spades":
                return "♠"
            case "clubs":
                return "♣"
            case _:
                return f" of {self.suit}"

    def __cardValue(self) -> int:
        match self.number:
            case 11:
                return 10
            case 12:
                return 10
            case 13:
                return 10
            case _:
                return self.number

    # Public functions
    
if __name__ == "__main__":
    c = Card(5, "hearts")
    print(c)