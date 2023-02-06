"""
File: prob1.py
Author: Derek Tominaga
Purpose: This program contains classes
and methods in the classes to perform
specifc tasks
Course: CSC 120, spring 2020
"""

class Simplest:
    def __init__(self, var1, var2, var3):
        self.a = var1
        self.b = var2
        self.c = var3

class Rotate:
    def __init__(self, first, second, third):
        self._first = first
        self._second = second
        self._third = third

    def get_first(self):
        return self._first
    def get_second(self):
        return self._second
    def get_third(self):
        return self._third

    def rotate(self):
        var1 = self._first
        var2 = self._second
        var3 = self._third
        self._first = var2
        self._second = var3
        self._third = var1

class Band:
    def __init__(self,singer):
        self._singer = singer
        self._drummer = None
        self._guitar_players = []

    def get_singer(self):
        return self._singer
    def set_singer(self, new_singer):
        self._singer = new_singer

    def get_drummer(self):
        return self._drummer
    def set_drummer(self, new_drummer):
        self._drummer = new_drummer

    def add_guitar_player(self, new_guitar_player):
        self._guitar_players.append(new_guitar_player)
    def fire_all_guitar_players(self):
        self._guitar_players = []
        return self._guitar_players
    def get_guitar_players(self):
        return self._guitar_players[:]

    def play_music(self):
        lineup = self._guitar_players
        if self._singer == "Frank Sinatra":
            print("Do be do be do")
        elif self._singer == "Kurt Cobain":
            print("bargle nawdle zouss")
        else:
            print("La la la")
        if self._drummer is not None:
            print("Bang bang bang!")
        for i in range(len(lineup)):
            print("Strum!")