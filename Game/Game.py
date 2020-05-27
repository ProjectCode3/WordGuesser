import random


class Game(object):
    def __init__(self, score, words, word,  round, correct_word, player_name):
        self.score = score
        self.words = []
        self.word = word
        self.round = round
        self.correct_word = correct_word
        self.playername = player_name

    def get_name(self):
        return self.playername

    def game_round(self):
        return self.round

    def set_game_round(self):
        for self.correct_Word in self.words:
            if self.word == self.correct_Word:
                self.round += 1
            elif not self.word == self.correct_Word:
                self.get_word()

    def get_word(self):
        self.correct_word = random.choice(self.words)
        return self.correct_word




