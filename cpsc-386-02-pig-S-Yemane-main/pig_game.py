# Shalom Yemane
# CPSC 386-01
# 2021-10-07
# syemane@csu.fullerton.edu
# @S-Yemane
#
# Lab 02-00
#
# This file represents the game object.
#

"""Game class for the program."""

from time import sleep
from die import Die
from player import Player


class PigGame:
    """A class responsible for all calculations and mechanisms of the game Pig."""

    def __init__(self):
        """Initializer"""
        self._die = Die()
        self._player_list = []
        # PigGame starts the game immediately upon initialization.
        self._make_players()
        self._order_selection()
        self._run()

    def _make_players(self):
        """Creates the Player objects."""
        # Ask how many players are playing.
        num_players = int(input('How many players are there? (1-4) '))

        # Check that the number entered is valid.
        while num_players > 4 or num_players < 1:
            num_players = int(
                input('There must be 1-4 players. How many players? ')
            )

        # Ask each player their name. Create the player object.
        for i in range(num_players):
            player = Player(
                str(input('Player {}, what is your name? '.format(i + 1)))
            )
            self._player_list.append(player)

        # Create an A.I. player if there is only one human player.
        if num_players == 1:
            print('Say hello to "Robot", your opponent!')
            self._player_list.append(Player('Robot', True))

    def _order_selection(self):
        """Decide the order of the players."""
        print('It is now time to decide the turn order of the players.')
        sleep(2)
        print('Each player will now have a die rolled for them.')
        sleep(2)
        print('Turn order will be decided by highest roll.')
        sleep(2)
        # Roll die for each player, then add to a list to be sorted.
        order_list = []
        for player in self._player_list:
            roll = self._die.roll()
            print('{}, you rolled a {}!'.format(player.name, roll))
            order_list.append((roll, player))
            sleep(0.5)

        # Sort the list by rolls, equal rolls are handled by the function.
        order_list.sort(key=lambda y: y[0])
        # Reverse order since sort() orders in ascending order.
        order_list.reverse()
        # Clear _player_list, then repopulate it with order_list.
        self._player_list.clear()
        for tup in order_list:
            self._player_list.append(tup[1])

        print('Player order is as follows:')
        print(*self._player_list)
        sleep(2)

    def _run(self):
        """Main game loop"""
        game_over = 0
        # Loop until there is a winner.
        while game_over != 1:
            # Loop over the player list, give each player a turn.
            for player in self._player_list:
                # Initialize variables for current turn score and # of times rolled.
                current_score = 0
                num_times_rolled = 0

                print('{}, it is your turn!'.format(player.name))
                sleep(2)
                # Loop for the current player's turn.
                while True:
                    player_input = ''
                    print(
                        'Total Score: {}. Current Score {}. You have rolled {} times!'.format(
                            player.score, current_score, num_times_rolled
                        )
                    )
                    sleep(1)

                    # Check if the current player is Robot.
                    if player.is_robot == True:
                        # Decide if Robot should roll or hold.
                        if num_times_rolled < 5 and current_score < 18:
                            player_input = 'r'
                        else:
                            player_input = 'f'

                    # Ask the player for input until they input a valid character.
                    while player_input != 'r' and (
                        player_input != 'f' or current_score == 0
                    ):
                        if num_times_rolled == 0:
                            player_input = input('Press "r" to roll the die. ')
                        else:
                            player_input = input(
                                'Press "r" to roll the die, or press "f" to end your turn. '
                            )

                    num_times_rolled += 1
                    # Perform player action.
                    if player_input == 'r':
                        roll = self._die.roll()
                        # If the player rolled a 1, end their turn.
                        if roll == 1:
                            print('You rolled a 1! Your turn is over!')
                            # break to exit the turn loop.
                            break

                        # If the player didn't roll a 1, add roll to current_score.
                        current_score += roll
                        print('You rolled a {}!'.format(roll))
                    else:
                        # Add current_score to the player's score, then end their turn.
                        player.add_score(current_score)
                        print(
                            '{}, you have ended your turn. Your total score is {}'.format(
                                player.name, player.score
                            )
                        )
                        # break to exit the turn loop.
                        break

                # Check if the current player won.
                if player.score >= 100:
                    game_over = 1
                    print(
                        'Congratulations, {}! You are the winner!'.format(
                            player.name
                        )
                    )
                    break
