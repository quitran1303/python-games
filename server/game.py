from .player import Player
from .board import Board
from .round import Round

class Game(object):
    def __init__(self, id, players):
        self.id = id
        self.players = []
        self.words_used = []
        self.round = None
        self.board = None
        self.player_draw_ind = 0
        self.start_new_round()

    def start_new_round(self):
        self.round = Round(self.get_word(), self.players[self.player_draw_ind])
        self.player_draw_ind += 1

        if self.player_draw_ind >= len(self.players):
            self.round_ended()
            self.end_game()

    def player_guess(self, player, guess):
        """
        Makes the player guess the word
        :param player: Player
        :param guess: str
        :return: bool
        """
        pass

    def player_disconnected(self, player):
        """
        Call to clean up objects when player disconnects
        :param player: Player
        :raises: Exception()
        """
        pass

    def skip(self):
        """
        Increments the round skips, if skips are greater than threshold, starts new round
        :return: None
        """
        if self.round:
            new_round = self.round.skip()
            if new_round:
                self.round_ended()
        else:
            raise Exception("No round started yet")

    def round_ended(self):
        self.round.skips = 0
        self.start_new_round()

    def update_board(self):
        pass
    
    def end_game(self):
        pass

    def get_word(self):
        """
        give a word that has not yet been used
        """
        ##TODO get a list of words from somewhere
        pass
