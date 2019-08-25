class Player:
    def __init__(self, figure):
        """
        Constructor

        :param figure: figure representing the player
        :type figure: logic.figure.Figure
        """
        self.cards = []
        self.figure = figure
        self.still_in_game = True
        self.STRATEGY = ""

    def set_game_reference(self, game):
        """
        Attach a reference to the central game logic object

        :param game: central game logic
        :type game: Game
        """
        self.game = game

    def set_own_card(self, card):
        self.cards.append(card)

    def __str__(self):
        return f"{self.figure.name} ({self.STRATEGY})"