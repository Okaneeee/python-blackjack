from __future__ import annotations

# hearts ♥ - diamonds ♦ - spades ♠ - clubs ♣

class Card:
    """Card of a deck

    Args:
        number (int): number of the card
        suit (str): suit of the card

    Attributes:
        number (int): number of the card
        suit (str): suit of the card
        value (int): value of the card     
    """
    # Constructor
    def __init__(self, number: int, suit: str) -> None:
        self.number: int = number
        self.suit: str = suit
        self.value: int = self.__cardValue()

    # Default functions
    def __repr__(self) -> str:
        """Return a string representation of the card

        Returns:
            str: string representation of the card
        """
        return f"{self.__numberFormat()}{self.__suitFormat()}"
    
    def __str__(self) -> str:
        """Return a string representation of the card

        Returns:
            str: string representation of the card
        """
        return self.__repr__()

    def __len__(self) -> int:
        """Return the length of the card string 

        Returns:
            int: length of the card string
        """
        return len(self.__str__())

    # Private functions
    def __numberFormat(self) -> str:
        """Make a good format for the number of the card

        Returns:
            str: the number of the card
        """
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
        """Make a good format for the suit of the card

        Returns:
            str: the suit of the card
        """
        # In case it's heart or diamond..., add an 's' at the end  
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
        """Return the value of the card

        Returns:
            int: the value of the card
        """
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