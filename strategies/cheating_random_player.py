import random

from strategies import RandomPlayer

# Probability for cheating in first round 1/1000, in second round 2/1000, ...
CHEATING_PROB = 1000.0


class CheatingRandomPlayer(RandomPlayer):
    """
    Like random player but manages with a certain growing probability to look into the crime cards
    and use that information for accusation then
    """

    def __init__(self, figure):
        super().__init__(figure)
        self.round_counter = 0
        self.STRATEGY = "CHEATING_RANDOM"

    def next_question(self):
        self.round_counter += 1

        # Randomly decide to cheat (with increasing probability during the game)
        if random.random() < self.round_counter / CHEATING_PROB:
            # Cheat (use the crime information from game object for accusation)
            self.current_question = (
                True,
                self.game.crime_figure,
                self.game.crime_weapon,
                self.game.crime_scene
            )
            return self.current_question
        else:
            # Do not cheat but use random player strategy
            return super().next_question()
