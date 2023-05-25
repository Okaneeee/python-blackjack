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
from time import sleep
from os import system

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
    """
    
    # Private attributes
    __enum: list[str] = []
    __firstTurn: bool = True
    __hasStand: bool = False
    __hasBust: bool = False
    __hasInsurance: bool = False
    __triggerInsurance: bool = False

    # Constructor
    def __init__(self, player: Player, dealer: Dealer = Dealer()) -> None:
        self.player: Player = player
        self.dealer: Dealer = dealer
        self.deck: Deck = Deck()

    # Default method
    def __str__(self) -> str:
        """Returns the game as a string

        Returns:
            str: the game as a string
        """
        return f"{self.player}\n{self.dealer}"

    # Public methods
    def resetGame(self) -> None:
        """Reset the game
        """
        self.player.reset()
        self.dealer.reset()
        self.deck.reset()

    def avalaibleActions(self) -> str:
        """Return the avalaible actions

        Returns:
            str: the avalaible actions
        """
        final: str = "HIT | STAND "
        self.__enum = ["hit", "stand"]

        if(self.__firstTurn and self.player.enoughMoney("double")):
            final = "DOUBLE | " + final # Can only double on first turn
            self.__enum.append("double")
        if(self.player.canSplit() and self.player.enoughMoney("split")):
            final += "| SPLIT " # Can only split if it's first turn and both cards are of the same value
            self.__enum.append("split")
        if(self.dealer.canInsurance() and self.player.enoughMoney("insurance") and self.__firstTurn and not self.__triggerInsurance):
            final += "| INSURANCE " # Can only insurance if it's first turn and the first card of the dealer is an ace or a 10
            self.__enum.append("insurance")

        final += '> '

        return final

    def showHands(self) -> None:
        """Show the hands of the player and the dealer
        """
        if(self.__hasStand or self.__hasBust or self.__hasInsurance):
            print(f"{self.player} ({self.player.handValue()})")
            print(f"{self.dealer} ({self.dealer.handValue()})")
        else:
            print(f"{self.player} ({self.player.handValue()})")
            self.dealer.displayHand()

    def betResults(self, winner: bool = None) -> None: # type: ignore
        """Show the bet results

        Args:
            winner (bool): True if player won, else False
        """
        if(winner == None):
            won = self.player.bet
            self.player.giveMoney(won)
            print(f"You got back your ${won}")
        elif(winner):
            if(self.__hasInsurance):
                won = self.player.bet * 2.5
                self.player.giveMoney(won) # type: ignore
                print(f"Congratulations! You and won: ${won}!")
            elif(self.player.hasBlackjack()):
                won = self.player.bet * 3
                self.player.giveMoney(won)
                print(f"Congratulations! You got a blackjack and won: ${won}!")
            else:
                won = self.player.bet * 2
                self.player.giveMoney(won)
                print(f"Congratulations! You won: ${won}!")
        else:
            print(f"Too bad! You lost ${self.player.bet}!")

    # Game phases methods
    def __startPhase(self) -> None:
        """Start the game
        """
        print("----> Game start")
        print(f"Player: {self.player.name}") # Player reminder
        print(f"Balance: ${self.player.balance}\n") # Balance reminder

    def __betPhase(self) -> None:
        """Bet phase
        """
        print("----> Bet phase")
        self.bet()
        betEnd = self.deal()
        while not (betEnd):
            self.bet()
            betEnd = self.deal()
        print(f"You bet ${self.player.bet}\n")
    
    def __results(self, dealerBust: bool = False) -> None:
        """Show the game results
        """
        print("----> Game results")
        self.showHands()
        print()
        if(self.__hasBust): # Player busted
            print("You busted! Dealer won")
            self.betResults(False)
        elif(self.__hasInsurance):
            print("Dealer had blackjack ! You won via insurance")
            self.betResults(True)
        elif(dealerBust): # Dealer busted
            print("Dealer busted! You won")
            self.betResults(True)
        elif(self.player.handValue() > self.dealer.handValue()): # Player won
            print("You won!")
            self.betResults(True)
        elif(self.player.handValue() == self.dealer.handValue()):
            print("Tie!")
            self.betResults()
        else: # Dealer won
            print("Dealer won!")
            self.betResults(False)

    def __playerTurn(self) -> None:
        """Player turn
        """
        sleep(0.4)
        print("--> Your turn\n")
        sleep(0.5)
        while not (self.__hasStand or self.__hasBust):
            # Showing both player's and dealer's hands
            self.showHands()

            # Asking for actions
            print("\nWhat do you want to do?")
            action = input(self.avalaibleActions()).lower()
            sleep(0.7)

            # Invalid action case
            if (action not in self.__enum):
                print("You can't do that!")
            else:
                match action:
                    case "stand":
                        self.stand()
                    case "insurance":
                        if(self.insurance()):
                            self.player.giveMoney(self.player.bet*2)
                            break
                        else:
                            print("Dealer doesn't have blackjack.")
                            sleep(0.5)
                    case "hit":
                        self.hit(self.player)
                        if(self.player.hasBust()):
                            self.__hasBust = True
                            break
                        sleep(0.4)
                    case "double":
                        self.double()
                        break
                    case "split":
                        print("Not implemented yet, sorry!")
                        pass

    def __dealerTurn(self) -> None:
        """Dealer turn
        """
        # Dealer can play if:
        #   - Player standed
        #   - It's not an insurance win
        #   - Player didn't bust
        #   - Player have a blackjack
        if (self.__hasStand and not self.__hasInsurance and not self.__hasBust and not self.player.hasBlackjack()):
            print("\n--> Dealer is playing!")
            self.showHands()
            sleep(0.6)
            while not (self.dealer.shouldStand()):
                print()
                self.hit(self.dealer)
                sleep(0.4)
                self.showHands()
                sleep(0.4)

    def __endPhase(self) -> None:
        """End of the game
        """
        print("----> Game end")
        replay = input("Do you want to play again? (Y/N) ").upper()
        sleep(0.5)
        if replay == 'Y':
            self.__clearTerminal()
            self.play()
        else:
            print("Goodbye!")
            exit()

    # Before game methods
    def bet(self) -> None:
        """Ask the player to bet
        """
        boo: bool = True
        while(boo):
            try:
                toBet = int(input(f"Bet: ${self.player.bet}   Balance: ${self.player.balance}\nHow much do you want to bet? "))
                self.player.setBet(toBet)
                boo = False
            except ValueError:
                print("You can't bet that much money!")

    def deal(self) -> bool:
        """Ask the player if he finished betting

        Returns:
            bool: True if the player finished betting, False otherwise
        """
        act = input(f"\nBet: ${self.player.bet}   Balance: ${self.player.balance}\nDid you finish your bet? (Y/N) ").upper()
        # NOTE: remove when interface
        while (act != "Y" and act != "N"):
            act = input(f"\nBet: ${self.player.bet}   Balance: ${self.player.balance}\nDid you finish your bet? (Y/N) ").upper()
        if act == "N":
            return False
        return True

    def start(self) -> None:
        """Deal the cards to the player and the dealer
        """
        for _ in range(2):
            c = self.deck.draw()
            self.player.addCard(c)
            c = self.deck.draw()
            self.dealer.addCard(c)

    # In-Game methods
    def split(self) -> list[Game]: # type: ignore
        """
        Not implemented yet
        
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
        self.__firstTurn = False
        ...

    def double(self) -> None:
        """
        Draw a card and double the bet
        """
        self.hit(self.player)
        self.player.setBet(self.player.bet)

        # Checking if player busted
        if(self.player.hasBust()):
            self.__hasBust = True
        else:
            self.stand()

    def hit(self, entity: Player | Dealer) -> None: 
        """Draw a card and add it to the entity's hand

        Args:
            entity (Player | Dealer): The entity that will draw a card
        """
        c = self.deck.draw()
        entity.addCard(c)
        self.__firstTurn = False
    
    def stand(self) -> None:
        """Basically end the "draw" phase
        """
        self.__hasStand = True # Ending turn

    def insurance(self) -> bool:
        """Check if dealer has blackjack
        Can only be called if dealer has an ace or a 10+ as first card

        Returns:
            bool: True if he has, else False
        """
        self.player.removeMoney(int(self.player.bet/2))
        self.__triggerInsurance = True
        if(self.dealer.hasBlackjack()):
            self.__hasInsurance = True
        return self.__hasInsurance

    # Private methods
    def __checkGame(self) -> None:
        """Check if the game status
        """

        # Resetting dealer, player and deck
        if(self.player.balance == 0):
            print("We're giving you back $1000\n")
            self.player.reset()
        if(self.player.bet > 0):
            self.player.bet = 0
        self.deck.reset()
        self.player.resetHand()
        self.dealer.reset()

        # Resetting game settings
        self.__firstTurn = True
        self.__hasStand = False
        self.__hasBust = False
        self.__hasInsurance = False
        self.__triggerInsurance = False

    def __clearTerminal(self) -> None:
        """Clear the terminal
        """
        system("cls||clear")

    # Main method
    def play(self) -> None:
        """Play the game
        """
        # Starting the game
        self.__startPhase()
        
        # Verifying game state
        self.__checkGame()
        
        sleep(0.7)

        # Starting bet phase
        self.__betPhase()

        sleep(0.7)

        # Starting game phase
        print("----> Game phase")
        self.start()

        # Player turn
        self.__playerTurn()

        # Dealer turn
        self.__dealerTurn()

        # Show results
        sleep(0.7)
        print()
        self.__results(self.dealer.hasBust())
        print()
        sleep(0.5)

        # End of the game
        self.__endPhase()

if __name__  == "__main__":
    pass