from strategies.player import Player


class RandomPlayer(Player):
    """
    Completely random decision based strategy
    """

    def __init__(self, figure):
        super().__init__(figure)
        self.STRATEGY = "RANDOM"
