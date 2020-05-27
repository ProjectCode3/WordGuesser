import random


class Game(object):
    def __init__(self, name, round, wordlist):
        self.name = name
        self.round = round
        self.wordlist = wordlist

    def set_name(self):
        return self.name

    def set_round(self):
        return self.round

    def set_list(self):
        return self.wordlist

    