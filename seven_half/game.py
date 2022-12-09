from seven_half.abc.counting_strategy import CountingStrategy


class Card:
    """This class is to represent a card of a Neapolitan deck"""

    def __init__(self, suit: str, number: int):
        """instantiate a new card"""
        self.suit: str = suit
        self.number: int = number
        self.value: float = number if number < 8 else 0.5


class Deck:
    #     @attributes
    #
    #     _available_cards        -> list[Card]
    #     _removed_cards          -> list[Card]
    #
    #     @methods
    #
    #     get_card()              -> list[Card]
    #     reset_deck()            -> None
    """This class represents a deck of Neapolitan cards. There are 4 seeds: Swords, Clubs, Coins, Cups and the
    numbers are from 1 to 10. the values of the cards are 0.5 if 8, 9, 10 and their natural value if numbers from 1-7
    the 10 of coins has a base value of 0.5 but can be worth whatever the owner decides."""

    def __init__(self):
        """Instantiate a Deck of neapolitan cards."""
        self._available_cards: list[Card] = []
        self._removed_cards: list [Card] = []

    def get_card(self) -> list[Card]:
        """
        Returns a list of cards from the deck.

        This method is a getter for the cards in the deck.
        """
        ...

    def reset_deck(self) -> None:
        """
        Resets the deck

        This method resets the deck to the original standard state.
        """
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
    """Represent a sette e mezzo table."""

    def __init__(self, deck: Deck):
        """Instantiate a new table."""
        self._score: dict[Player, int] = {}
        self._deck: Deck = deck

    def get_players(self) -> list[Player]:
        """
        Returns the list of players

        this method is a getter of the list of players
        """
        ...

    def add_players(self, *players) -> None:
        """
        Add a player or multiple players

        This method adds a single player, or multiple players to the table
        """
        ...

    def remove_players(self, *players) -> None:
        """
        Remove a player or multiple players

        This method removes a single player, or multiple players to the tabl
        """
        ...

    def get_score(self) -> dict[Player, int]:
        """
        Returns the score as a dictionary

        This method is a getter of the score, which is returned as a dictionary with a player as a key and an int as
        value
        """
        ...

    def increase_score(self, player: Player, add: int) -> None:
        """
        Increase the score of a player by a certain amount

        This method increases the score of a player by the amount specified in the argument variable add
        """
        ...

    def reset_score(self) -> None:
        """
        Reset the score to zero

        This method resets the score to zero
        """
        ...

    def get_deck(self) -> Deck:
        """
        Returns the deck

        This method is a getter of the deck asociated with this table
        """
        ...

    def get_cards_from_deck(self) -> Card:
        """
        Return the next card in the deck

        This method takes a card from the deck each time is called
        """
        ...

    def calculate_round_result(self) -> None:
        """
        Evaluates the result of the round

        This method calculates the round result in order to keep track of the score
        """

    def new_round(self) -> None:
        """
        Initiates a new round

        This methods is used to start a new round of sette e mezzo
        """