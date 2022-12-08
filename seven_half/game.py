from typing import List, Any

from seven_half.abc.counting_strategy import CountingStrategy


class Card:
    ...


class Deck:
    ...


class Player:
    """Represent a player at a sette e mezzo table."""

    def __init__(
            self,
            counting_strategy: CountingStrategy,
    ):
        """Instantiate a new player."""
        self._hand: list[Card] = []
        self._counting_strategy = counting_strategy
        self._table: Table = None

        self.dealer = False
        self.bet_amount: float = 0.0
        self.lost = False

    def bet(self, amount: float) -> None:
        """
        Set the player's bet amount for this round.
        
        This method sets the Player object's bet_amount attribute to the bet amount.
        """
        ...

    # Actions in round
    def request_card(self) -> None:
        """
        Request a card from the dealer.

        Since the dealer in sette e mezzo is a player without special privileges, this behaviour can
        be simplified to `self.table.get_card()` and adding the card to `self.hand`.
        """
        ...

    def quit(self) -> None:
        """
        Quit the round.

        This method sets the Player object's lost attribute to True.
        """
        ...

    def change_4_card(self) -> None:
        """
        Change the 4-card in player's hand for a new one.

        This behaviour is only valid for the first card dealt. If this method is called after the
        first card, it is ignored.
        """
        ...

    def set_wild_card(self, value: int) -> None:
        """
        Set a wild card's value.

        Wildcard is defined as the 10 of Coins. This method is only valid when the player has a
        wildcard in their hand. If the player does not have a wildcard, this method is ignored.
        """
        ...

    def declare_loss(self) -> None:
        """
        Declare loss from exceeding 7.5 pts in a round.

        This method sets the Player object's lost attribute to True.
        """
        ...

    def turn(self) -> None:
        """
        Simulate a player's turn in a round.

        This method implements the player's decision logic, and is the primary interaction
        method between the player and the game.
        """
        ...

    def reset(self) -> None:
        """
        Reset the player's attributes for a new round.

        This method resets the player's hand, lost attribute, and bet amount.
        """
        ...

    def check_card(self) -> Card:
        """
        Check the first card in the player's hand.

        This method returns the first card in the player's hand only. This is to simulate the
        real life behaviour in a game of sette e mezzo, where all players can only see the first
        card in each other's hand.
        """
        ...


class Table:
    """Represent the table where the game happens."""

    def __init__(self, deck: Deck):
        """Instantiate a new table."""
        self._players: list[Player] = []
        self._score: dict[Player, int] = {}
        self._deck: Deck = deck

    def get_players(self) -> list[Player]:
        """returns the list of players"""
        return self._players

    def add_players(self, *players) -> None:
        """add a player or multiple players"""
        for player in players:
            self._players.append(player)

    def remove_players(self, *players) -> None:
        """remove a player or multiple players"""
        for player in players:
            self._players.remove(player)

    def get_score(self) -> dict[Player, int]:
        """returns the score as a dictionary"""
        return self._score

    def increase_score(self, player: Player, add: int) -> None:
        """increase the score of a player by a certain amount"""
        self._score[player] += add

    def reset_score(self) -> None:
        """reset the score to zero"""
        self._score = 0

    def get_deck(self) -> Deck:
        """returns the deck"""
        return self._deck

    def get_cards_from_deck(self) -> Card:
        """return the next card in the deck"""
        yield from self._deck
