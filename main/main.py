from Game.Game import Game
import random
import time as t


def start_game():
    round = 0
    playername = input("Enter A player Name: ")
    wordlist = ["save", "amused"]

    game = Game(playername, round, wordlist)

    print(f"Current Player: {game.set_name()}")
    t.sleep(1)
    print(f"Current Round: {game.set_round()}")
    t.sleep(1)
    print(f"List: {game.set_list()}")


start_game()
