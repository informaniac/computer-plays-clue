import random

from strategies.random_player import RandomPlayer
from logic.card import CardType

NUM_OF_CARDS = 21                           # there are 21 cards in the game
NUM_OF_CARDS_ON_PLAYERS = NUM_OF_CARDS - 3  # of which 3 have been removed


class LearnsStuffPlayer(RandomPlayer):
    def __init__(self, figure):
        super().__init__(figure)
        self.STRATEGY = "ALSO MEMORIZE SETS OF CARD(S) THAT PLAYERS COULD HAVE SHOWN"  # but does not resolve this, yet
        self.knows_weapon = False
        self.solution_weapon = ""
        self.knows_room = False
        self.solution_room = ""
        self.knows_figure = False
        self.solution_figure = ""
        self.num_own_cards = len(self.cards)
        self.my_questioned_cards = []         # temporarily stores the rounds guess ["card", "card", "card"]
        self.my_questioned_combinations = []  # [["card", "card", "card"]...]
        self.my_uncertainties = []            # uncertainty: ("player", ["card"...])
        self.num_other_players_cards = None   # if amount of cards is balanced, each player gets the same amount
        # check if we can determine how many cards each player has
        if NUM_OF_CARDS_ON_PLAYERS % len(self.game.players) is 0:
            self.game_is_balanced = True
            self.game_is_balanced_only_for_me = False
            self.num_other_players_cards = NUM_OF_CARDS_ON_PLAYERS / len(self.game.players)
        elif (NUM_OF_CARDS_ON_PLAYERS - self.num_own_cards) % len(self.game.players - 1) is 0:
            self.game_is_balanced = True
            self.game_is_balanced_only_for_me = True
            self.num_other_players_cards = (NUM_OF_CARDS_ON_PLAYERS - self.num_own_cards) / len(self.game.players - 1)
        else:
            self.game_is_balanced = False
            self.game_is_balanced_only_for_me = False

    # OVERRIDDEN
    def see_no_card_from_nobody(self):
        for card in self.my_questioned_cards:
            if not self.is_own_card(card):
                self.mark_for_solution(card)

    def is_own_card(self, card):
        """
        Check if given card is your own card
        :param card: card in question
        :return: card in self.cards: bool
        """
        return card in self.cards

    def mark_for_solution(self, card):
        card_type = self.game.get_card_type(card)
        if card_type is CardType.FIGURE:
            self.knows_figure = True
            self.solution_figure = card
            self.unknown_figures = [card]
        elif card_type is CardType.WEAPON:
            self.knows_weapon = True
            self.solution_weapon = card
            self.unknown_weapons = [card]
        elif card_type is CardType.ROOM:
            self.knows_room = True
            self.solution_room = card
            self.unknown_rooms = [card]

    def knows_solution(self):
        return self.knows_figure and self.knows_figure and self.knows_room

    # OVERRIDDEN
    def next_question(self):
        if self.knows_solution():
            return True, self.solution_figure, self.solution_weapon, self.solution_room
        # TODO: guess smarter
        else:
            accusation, guessed_figure, guessed_weapon, guessed_room = super().next_question()
            self.my_questioned_cards = []
            self.my_questioned_cards.append(guessed_figure)
            self.my_questioned_cards.append(guessed_weapon)
            self.my_questioned_cards.append(guessed_room)
            self.my_questioned_combinations.append(self.my_questioned_cards)
            return accusation, guessed_figure, guessed_weapon, guessed_room
