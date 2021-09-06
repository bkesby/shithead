# Game Mechanics #

Document that will outline all game mechanics and rules that must be created. This can be used as a scratchpad for pseudocode and object definitions but should eventually become a game rules document by v1.0.

## Rules ##

#### Wiki ####

Wiki game definition:

    "Shithead (also known by many other names, most commonly Karma, Palace and Shed) is a card game, the object of which is to lose all of one's playing cards, with the final player being the "shithead"."

Wiki setup:

    "From a standard, shuffled deck of cards, each player is dealt 9 cards in total: 3 face-down cards in a row (blind cards), 3 face-up cards on top of the blind cards, and 3 hand cards. The blind cards will be the last cards to be played and players are not allowed to see or change these cards until the ending turns of the game. The face-up will be the second to last set of cards to be played in the game (before the blind cards). At the beginning of the game, players are allowed to switch their hand cards with their face-up cards in an attempt to produce a strong set of face-up cards (possibly all perfect wildcards) for later in the game. Cards with the same numerical value can be stacked on top of each other if needed."

#### Definitions ####

It will be good to have game definitions outlined early to help with documentation and code commentary. Change these as desired.

- __Game__ : A (un)defined series of rounds.

- __Round__: One completion of all cycles of play from all cards being dealt until all but one player has played all their available cards.

- __Cycle__: Measured as the start of player index one starting a turn to the end of player index -1 finishing their turn. Relevant for '3' rules when bringing a player back in. 

- __Turn__: Time in which a player makes legal moves. There is only ever one turn at a time.

- __Card__: A game card. Defined range of values. All cards are unique.

- __Deck__: All cards that have not yet been dealt or picked up by any player yet. [Should be a generator of sorts. Only ever deals next card.]

- __Stack__: All face up cards played on previous turns. Determines the field of available cards.

- __Discard__: All cards taken out of play.

- __Down__: 3 start cards that are unknown to all players until flipped and played.

- __Top__: 3 start cards that are visible to all players. Must all be played before __Down__ cards can be played.

- __Hand__: All cards in control of an individual player except __Down__ cards or __Top__ cards.

- __Playable__: Any cards player cards that can be played into the __Stack__. This is determined by the last entry in the __Stack__ and the __Card__ position.

- __Card_Position__: Describes the state of play/location of the card that will determine rules that can be applied to the card.

- __Player__: A participant of the game.

- __Dealer__: Manager of the game. Initializes each __Round__ and manages __Turn__ ordering.

## PseudoCode ##

This is my attempt to formulise some way of creating these game mechanics.

Notes: [BK] I'm not sure yet whether the state of the card or card position should be stored in the card itself or handled by the dealer instead. I like the idea of a card object being a simple immutable data class, but having card state will probably make things a lot easier when it comes to turn actions.

##### Models #####

__Card__: Should be nothing more than a data class that holds card value properties. No two __cards__ should have the same values. Once a __card__ is created it shouldn't be deleted and reinitialized in a __game__.

__Dealer__: This should be treated as the game manager and hold all commands and logic for running the game. Should only ever be initialized once per game. Should only ever be one __dealer__. Should create the shuffled deck.

__Player__: Should hold all actions and commands that a player would issue. Should be seen as a controller for turn actions that are issued to the __dealer__.


##### Actions #####

__Card__: None

__Player__:
    - Play a card.
    - Select starting cards.

__Dealer__:
    - Shuffle deck.
    - Assign cards to each player.
    - Issue player turn.




