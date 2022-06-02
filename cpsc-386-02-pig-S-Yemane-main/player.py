# Shalom Yemane
# CPSC 386-01
# 2021-10-07
# syemane@csu.fullerton.edu
# @S-Yemane
#
# Lab 02-00
#
# This file represents a single player in the game.
#

"""Player class for the program."""


class Player:
    """A class representing a single player in the game."""

    def __init__(self, name, is_robot=False):
        """Initializer"""
        self._name = name
        self._is_robot = is_robot
        self._score = 0

    @property
    def is_robot(self):
        """is_robot variable getter"""
        return self._is_robot

    @property
    def name(self):
        """name variable getter"""
        return self._name

    @property
    def score(self):
        """score variable getter"""
        return self._score

    def add_score(self, amount):
        """Increment score by an amount."""
        self._score += amount

    def __str__(self):
        return '{}'.format(self.name)
