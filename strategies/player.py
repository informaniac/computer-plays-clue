import abc


class Player(abc.ABC):
    def __init__(self, figure):
        """
        Constructor

        :param figure: figure representing the player
        :type figure: logic.figure.Figure
        """
        self.cards = set()
        self.figure = figure
        self.still_in_game = True
        self.STRATEGY = ""
        self.game = None

    def set_game_reference(self, game):
        """
        Attach a reference to the central game logic object

        :param game: central game logic
        :type game: Game
        """
        self.game = game

    def set_own_card(self, card):
        """
        Set the given card as an own card

        :param card: card (figure, weapon or room)
        :type card: str
        """
        self.cards.add(card)

    def game_play_starts(self):
        """
        Game playing starts (all cards were given to the players, next the first player will throw a dice)
        """
        pass

    @abc.abstractmethod
    def next_room(self, possible_rooms):
        """
        Decide where to go next (based on possible next rooms)

        :param possible_rooms: list of possible rooms to go next (sorted by distance ascending)
        :type possible_rooms: list[str]
        :return: room to go to
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def next_question(self):
        """
        Ask question (or accuse)

        :return: Accuse (yes/no), figure, weapon, room
        :rtype: bool, str, str, str
        """
        pass

    @abc.abstractmethod
    def choose_card_to_show(self, questioned_cards):
        """
        Choose which card to show (if possible -- possessing at least one of the questioned cards)

        :param questioned_cards: list of cards curently asked for
        :type questioned_cards: list[str]
        :return: a card (or None) if player owns no match
        :rtype: str
        """
        pass

    @abc.abstractmethod
    def see_card(self, card, showing_player):
        """
        The given card is shown to the player by the showing player

        :param card: card the player sees
        :type card: str
        :param showing_player: player that shows the card
        :type showing_player: Player
        """
        pass

    @abc.abstractmethod
    def see_no_card(self, showing_player):
        """
        Player sees that showing player cannot present a card

        :param showing_player: player (not) showing a card
        :type showing_player: Player
        """
        pass

    @abc.abstractmethod
    def see_no_card_from_nobody(self):
        """
        Player sees that none of the players they asked showed a card
        """
        pass

    @abc.abstractmethod
    def observe_card_shown(self, showing_player, seeing_player, questioned_cards):
        """
        Observe that one player showed a card to another player (but not which card)

        :param showing_player: player showing the card
        :type showing_player: Player
        :param seeing_player: player seeing the card
        :type seeing_player: Player
        :param questioned_cards: list of cards the player asked for
        :type questioned_cards: list[str]
        """
        pass

    @abc.abstractmethod
    def observe_no_card_shown(self, showing_player, seeing_player, questioned_cards):
        """
        Observe that the player did not show a card to the questioning player

        :param showing_player: player obligated to show the card
        :type showing_player: Player
        :param seeing_player: player asking
        :type seeing_player: Player
        :param questioned_cards: list of cards the player asked for
        :type questioned_cards: list[str]
        """
        pass

    @abc.abstractmethod
    def observe_no_card_from_nobody(self, seeing_player, questioned_cards):
        """
        Observe that the none of the asked players showed a card to the questioning player

        :param seeing_player: player asking
        :type seeing_player: Player
        :param questioned_cards: list of cards the player asked for
        :type questioned_cards: list[str]
        """
        pass

    def __str__(self):
        return f"{self.figure.name} ({self.STRATEGY})"
