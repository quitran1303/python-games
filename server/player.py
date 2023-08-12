"""
Player object
"""

from .game import Game

class Player(object):
    def __init__(self, ip, name):
        """
        init the player object
        :param ip: str
        :param name: str
        """
        self.game = None
        self.ip = ip
        self.name = name
        self.score = 0

    def set_game(self, game):
        """
        set the players game association
        :param game: Game
        :return: None
        """
        self.game = game

    def update_score(self, x):
        """
        update the player score
        :param x:
        :return:
        """
        self.score = x
    
    def guess(self, wrd):
        """
        Makes a player guess
        :param wrd: string
        :return: bool
        """
        return self.game.player_guess(self, wrd)

    def disconnect(self):
        """
        Call to disconnect player
        :return: None
        """
        pass

    def get_score(self):
        """
        get player score
        :return: int
        """
        return self.score
    
    def get_name(self):
        """
        get player name
        :return: str
        """
        return self.name
    
    def get_ip(self):
        """
        gets player IP address
        :return: str
        """
        return self.ip