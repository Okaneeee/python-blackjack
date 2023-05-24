from __future__ import annotations

from cards import Card

class Player:
    """Player of the game

    Args:
        name (str): Name of the player
        balance (str, optional): Current balance of the player (Defaults to 1000)

    Attributes:
        name (str): Name of the player
        suit (str): Current balance of the player
        hand (list[Card]): Cards in the player hand
        betted (int): Betted money  
    """

    # Constructor
    def __init__(self, name: str, balance: int = 1000) -> None:
        self.name: str = name 
        self.balance: int = balance

        self.hand: list[Card] = []
        self.bet: int = 0

    # Default methods
    def __str__(self) -> str:
        return f"{self.name} has {self.hand}"

    # Public methods
    def setBet(self, value: int) -> None:
        if value > self.balance:
            raise ValueError("Bet value is higher than the player balance")
        self.balance -= value
        self.bet = value

    def handValue(self) -> int:
        # Empty hand case
        if len(self.hand) == 0:
            return 0

        # Sorting the hand in order to take the best value of the ace (also removing sensitivity to the addition order)
        playerHand = sorted(self.hand, key=lambda x: x.value, reverse=True)
        total: int = 0
        for card in playerHand:
            # If it's an ace
            if card.value == 1:
                # And the hand value is higher than 11
                # Then ace's value is 1 (can't be 11, otherwise the hand value would be 22+)
                # Else ace's value is 11
                total += 1 if total >= 11 else 11
            # Otherwise we add the card default value
            else:
                total += card.value
        return total


class Dealer:
    """Dealer of the game

    Args:
        name (str, optional): Name of the dealer (Defaults to "Dealer")

    Attributes:
        name (str): Name of the dealer
        hand (list[Card]): Cards in the dealer hand  
    """

    # Constructor
    def __init__(self, name: str = "Dealer") -> None:
        self.name : str = name
        self.hand: list[Card] = []

    # Default functions
    def __str__(self) -> str:
        return f"{self.name} has {self.hand}"
    
    def handValue(self):...

# Test part
if __name__ == "__main__":
    c1 = Card(1, "hearts")
    c2 = Card(13, "diamonds")
    c3 = Card(5, "clubs")

    # Player hand tests
    p = Player("Player")
    print(p.handValue()) # Should be 0
    print(p) # Should be []
    print("\n")


    p.hand = [c1, c2] 
    print(p.handValue()) # Should be 21
    print(p) # Should be [A♥, K♦]
    print("\n") 

    p.hand = [c1, c2, c3]
    print(p.handValue()) # Should be 16
    print(p) # Should be [A♥, K♦, 5♣]