from game import Game
from player import Player


if __name__  == "__main__":
    print("Welcome to blackjack !")
    playerName: str = input("What's your name ?\n> ")

    try:
        baseMoney: int = int(input("How much money would you like to start with? (Default to $1000)\n> "))
    except ValueError:
        baseMoney = 1000

    print("Good luck !")
    g = Game(Player(playerName, baseMoney))
    g.play()