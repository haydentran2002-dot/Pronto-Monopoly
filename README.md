# Pronto-Monopoly
Hi, this is my repository for the monopoly coding test :)

## Key rules identified (MUST HAVES AND REMEMBER!!!)
- 4 players in a fixed order
- Each player starts with 16 dollars
- Passing GO square gives 1 dollar
- Players are required to purchase any property they land on (if possible, refer to assumptions). 
- Traditional Monopoly mechanics such as auctions or declining purchases are not implemented
- Rent doubles if full colour set is owned
- Game ends when ANY player is bankrupt

## Assumptions and interpretations
- Game ends immediately when player becomes bankrupt
- No skipping purchases or auctioning if player has enough money (this one is implied as there is no other option either buy or cant)
- No other Monopoly rules
- Rent is equal to property price unless monopoly achieved (player owns all of that colour)
- When landing or crossing GO, the player receives 1 dollar
- If player lands on a square that is unowned AND does not have enough money, simply skip their turn. Only declare bankruptcy when needing to pay another player. This means that square will remain UNOWNED
- If there is a tie in most money all players count as winners (even if they still need a turn, the game automatically terminates when one enters bankruptcy)

## My plan and thoughts for solving this problem
1. Load board from the json
2. Represent the players and properties
3. Implement movement logic
4. Implement property purchase
5. Implement rent logic
6. Add monopoly rule
7. Add bankruptcy condition
8. Simulate game loop

## Design Decisions
- Used an object orientated design with Game, Player and Property classes for clarity and extensibility
- Game class manages the core simulation logic and flow
- Turn order is handled using modulo arithmetic on the player list
- Rent calculation is isolated in its own function for clarity and mainability

## How to run the Code
1. Ensure Python 3.9+ is installed
2. Navigate into the project folder: cd monopoly
3. Run the simulation: python main.py
4. If additional rolls or board states want to be used simply replace the names (These must be in the same format as the classes have been set in a certain way).

## How to test the code individually
At the bottom of the main.py file, I left the testing environment I used to test the functions individually, so if this code were to be further extended I could refer back to them.

## Extensibility
The system is designed to be easily extendable:

- New space types can be added
- Any additional rules/functions can be put into the Game class
- Player decision making (e.g optional purchases) could be introduced
- Board configuration can be modified via JSON without changing code

## Testing Approach

The system was primarily tested using small, targeted test cases after implementing each core component, followed by full end-to-end simulation using the provided roll sequences.

While the core logic was validated and produced correct results, most of the testing was conducted after implementing the main functionality rather than strictly during each incremental development step.

## Reflection

In hindsight, a more robust approach would have been to test each function immediately as it was developed (e.g. movement, property handling, rent calculation), rather than relying more heavily on end-to-end validation.

Testing incrementally would have:
- Made it easier to isolate and debug issues earlier
- Reduced the need to reason about multiple interacting components at once
- Improved confidence in each individual unit of logic

## Future Improvements

In future projects, I would:
- Introduce lightweight unit tests alongside each feature as it is developed
- Validate edge cases (e.g. bankruptcy, monopoly rent) immediately after implementation
- Maintain a clearer separation between unit-level testing and full simulation testing

This would result in a more test-driven and reliable development process.