# seven-and-half

Client request: Simulate a card game and test various card counting strategy

Game: Sette e mezzo
Target: Must not exceed 7.5 pts.
Card deck: 1-10; 4 suits: Swords, Cups, Coins, Batons.
Card values:
    - JQK counts as 0.5 pts.
    - 4 can be exchanged once.
    - 10 of Coin == Wildcard value.
Player win condition:
    - Natural 7.5 only if dealer not 7.5.
    - Must score higher than dealer without higher than 7.5.
    - Dealer larger than 7.5.
    * (Dealer wins if no winning conditions are satisfied.)
Rules:
    - First cards dealt is always hidden.
    - Subsequent cards are public.
    - Calculation starts once all players (including dealer) declare stopping.
    - Losses must be declared immediately.
    - Victory is only declared after all cards are calculated.
    - If player wins with 7.5, and hand contains a 10 of Coin, playe becomes dealer.

Behaviour:
    - Player:
        - Choice:
            - Change 4 (once).
            - Request card.
            - Quit round.
        - Automatic:
            - Declare loss.
            - Become 
        - Subsystem:
            - Counting strategy.

Counting strategy specification:
    - decide()  -> Take information about player's hand and hand state and table's state.
                -> Return literal "draw_card", "change_card", "quit" as decision.
