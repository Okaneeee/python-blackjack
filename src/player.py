from __future__ import annotations

from cards import Card

class Player:
    """Player of the game

    Args:
        name (str): Name of the player
        balance (str): Current balance of the player (Optional, defaults to 1000)

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
        """Return the player as a string

        Returns:
            str: the player as a string
        """
        return f"{self.name} has {self.hand}"

    def __len__(self) -> int:
        """Return the length of the player hand

        Returns:
            int: length of the player hand
        """
        return len(self.hand)

    # Public methods
    def setBet(self, value: int) -> None:
        self.balance -= value
        self.bet += value

    def handValue(self) -> int:
        """Returns the value of the player hand

        Returns:
            total (int): Value of the player hand        
        """
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
    
    def addCard(self, card: Card) -> None:
        """Add a card to the player hand

        Args:
            card (Card): Card to add to the player hand
        """
        self.hand.append(card)

    def reset(self) -> None:
        """Reset the player hand and bet
        """
        self.resetHand()
        self.__resetBet()
        self.balance = 1000

    def removeMoney(self, value: int) -> None:
        self.balance -= value

    def giveMoney(self, value: int) -> None:
        self.balance += value

    # Verification method
    def canSplit(self) -> bool:
        """Tell if the player can split his hand

        Returns:
            bool: True if the player can split his hand, False otherwise
        """
        # len(self.hand) == 2 : first turn, in case he draw another card next turn 
        # value == 10 : can only split if both cards have the same value
        return (len(self.hand) == 2 and (self.hand[0].value == self.hand[1].value))
    
    def enoughMoney(self, case: str) -> bool:
        """Tell if the player has enough money to do the action

        Args:
            case (str): Case of the action (insurance, split, double)

        Returns:
            bool: True if the player has enough money, False otherwise
        """
        match case:
            case "insurance":
                return self.balance >= self.bet / 2 # Insurance only take half of the betted money to check
            case "split":
                return self.balance >= self.bet # Split place your original bet with one hand and place an equal bet on the second
            case "double":
                return self.balance >= self.bet # Double multiply the bet by 2
            case _: # Wrong case
                return False

    def hasBlackjack(self) -> bool:
        """Tell if the player has a blackjack

        Returns:
            bool: True if the player has a blackjack, False otherwise
        """
        return (self.handValue() == 21 and len(self.hand) == 2)
    
    def hasBust(self) -> bool:
        """Tell if the player has a bust

        Returns:
            bool: True if the player has a bust, False otherwise
        """
        return (self.handValue() > 21)

    # Private methods
    def resetHand(self) -> None:
        """Reset the player hand
        """
        self.hand = []

    def __resetBet(self) -> None:
        """Reset the player bet
        """
        self.bet = 0

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

    # Default methods
    def __str__(self) -> str:
        """Return the dealer as a string

        Returns:
            str: the dealer as a string
        """
        return f"{self.name} has {self.hand}"

    def __len__(self) -> int:
        """Return the length of the dealer hand

        Returns:
            int: length of the dealer hand
        """
        return len(self.hand)

    # Public methods
    def handValue(self) -> int:
        """Returns the value of the dealer hand

        Returns:
            total (int): Value of the dealer hand        
        """
        # Empty hand case
        if len(self.hand) == 0:
            return 0

        # Sorting the hand in order to take the best value of the ace (also removing sensitivity to the addition order)
        dealerHand = sorted(self.hand, key=lambda x: x.value, reverse=True)
        total: int = 0
        for card in dealerHand:
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
    
    def addCard(self, card: Card) -> None:
        """Add a card to the dealer hand

        Args:
            card (Card): Card to add to the dealer hand
        """
        self.hand.append(card)

    def reset(self) -> None:
        """Reset the dealer hand
        """
        self.hand = []

    def displayHand(self) -> None:
        """Display the dealer hand (with the first card hidden)
        """
        if (self.hand[0].value != 1): # Default case
            print(f"Dealer has [{self.hand[0]}, ?] ({self.hand[0].value})")
        else: # Ace case
            print(f"Dealer has [{self.hand[0]}, ?] (11)")
    
    # Verification methods
    def canInsurance(self) -> bool:
        """Tell if the player can do an insurance based on the dealer hand

        Returns:
            bool: True if the player can do an insurance, False otherwise
        """
        return (len(self.hand) == 2 and self.hand[0].value == 1)

    def hasBlackjack(self) -> bool:
        """Tell if the dealer has a blackjack

        Returns:
            bool: True if the dealer has a blackjack, False otherwise
        """
        return (self.handValue() == 21 and len(self.hand) == 2)
    
    def hasBust(self) -> bool:
        """Tell if the dealer has a bust

        Returns:
            bool: True if the dealer has a bust, False otherwise
        """
        return (self.handValue() > 21)

    def shouldStand(self) -> bool:
        """Tell if the dealer should stand

        Returns:
            bool: True if the dealer should stand, False otherwise
        """
        return (self.handValue() >= 17)

# Test part
if __name__ == "__main__":
    c1 = Card(1, "hearts")
    c2 = Card(13, "diamonds")
    c3 = Card(5, "clubs")
    c4 = Card(10, "spades")
    c5 = Card(12, "hearts")

    # Player hand tests
    print("===== Player tests =====")
    p = Player("Player")
    print(f"Hand value: {p.handValue()}") # Should be 0
    print(p) # Should be []
    print()

    p.hand = [c1, c2] 
    print(f"Hand value: {p.handValue()}") # Should be 21
    print(p) # Should be [A♥, K♦]
    print() 

    p.hand = [c1, c2, c3]
    print(f"Hand value: {p.handValue()}") # Should be 16
    print(p) # Should be [A♥, K♦, 5♣]
    print()

    p.hand = [c4, c5]
    print(f"Hand value: {p.handValue()}") # Should be 20
    print(f"Split: {p.canSplit()}") #Should be true
    print(p) # Should be [10♠, Q♥]
    print()

    p.setBet(1000)
    p.hand = [c4, c5]
    print(p.enoughMoney("insurance")) # Should be false
    print(p.enoughMoney("split")) # Should be false
    print() 

    # Dealer hand tests
    print("===== Dealer tests =====")
    d = Dealer()
    d.hand = [c1, c2]
    print(f"Hand value: {d.handValue()}") # Should be 21
    print(f"Insurance: {d.canInsurance()}") # Should be true
    print(f"Blackjack: {d.hasBlackjack()}") # Should be true
    d.displayHand() # Should be [A♥, ?]
    print(d) # Should be [A♥, K♦]
    print()

    d.hand = [c1, c2, c3]
    print(f"Hand value: {d.handValue()}") # Should be 16
    print(f"Insurance: {d.canInsurance()}") # Should be false
    print(f"Blackjack: {d.hasBlackjack()}") # Should be false
    d.displayHand() # Should be [A♥, ?]
    print(d) # Should be [A♥, K♦, 5♣]
    print()