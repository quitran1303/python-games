import time as t
from _thread import *
from .game import Game
from .chat import Chat

class Round(object):
    def __init__(self, word, player_drawing, players):
        self.word = word
        self.player_drawing = player_drawing
        self.player_guessed = []
        self.skips = 0
        self.play_scores = {player:0 for player in players}
        self.time = 75
        self.chat = Chat(self)
        start_new_thread(self.time_thread, ())

    def skip(self):
        """
        Return true if round skipped threshold met
        :return: bool
        """
        self.skips += 1
        ##Where the self.players??
        if self.skips > len(self.players) - 2:
            self.skips = 0
            return True

        return False

    def time_thread(self):
        while self.time > 0:
            t.sleep(1)
            self.time -= 1
        self.end_round("Time is up")

    def guess(self, player, wrd):
        """
        return bool if play got guess correct
        """
        correct = wrd == self.word
        if correct:
            self.player_guessed.append(player)
            #TODO implement scoreing system here
            
    def player_left(self, player):
        """
        remove player that left from scores and list
        """

        if player in self.play_scores:
            del self.play_scores[player]

        if player in self.player_guessed:
            self.player_guessed.remove(player)

        if player == self.player_drawing:
            self.end_round()

    def end_round(self,msg):
        #TODO implement end_round functionality
        pass