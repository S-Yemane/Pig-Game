# Shalom Yemane
# CPSC 386-01
# 2021-10-07
# syemane@csu.fullerton.edu
# @S-Yemane
#
# Lab 02-00
#
# This file represents a 6-sided die object.
#

"""Die class for the program."""

from random import randint


class Die:
    """A class representing a 6-sided die."""

    def __init__(self):
        """Initializer"""

    def roll(self):
        """Returns a random int from 1 to 6, inclusive."""
        return randint(1, 6)
