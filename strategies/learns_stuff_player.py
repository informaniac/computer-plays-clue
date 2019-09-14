import random

from strategies.random_player import RandomPlayer
from logic.card import CardType


class LearnsStuffPlayer(RandomPlayer):
    def __init__(self, figure):
        super().__init__(figure)
        self.STRATEGY = "AT LEAST LEARNS SOMETHING IF NOBODY SHOWS CARDS"
        self.knows_weapon = False
        self.solution_weapon = ""
        self.knows_room = False
        self.solution_room = ""
        self.knows_figure = False
        self.solution_figure = ""
        self.my_questioned_cards = []
        self.my_questioned_combinations = []

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
