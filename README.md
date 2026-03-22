# Pronto-Monopoly
Hi, this is my repository for the monopoly coding test :)


# Key rules identified (MUST HAVES AND REMEMBER!!!)
- 4 players in a fixed order
- Each player starts with 16 dollars
- Passing GO square gives 1 dollar
- Players are reqquired to purchase any property they land on. Traditional Monopoly mechanics such as auctions or declining purchases are not implemented
- Rent doubles if full colour set is owned
- Game ends when ANY player is bankrupt

## Assumptions and interpretations
- Game ends immediately when player becomes bankrupt
- No skipping purchases or auctioning if player has enough money (this one is implied as there is no other option either buy or cant)
- No other Monopoly rules
- Rent is equal to property price unless monopoly achieved
- When landing or crossing GO, the player receives 1 dollar
- If player lands on a square that is unowned AND does not have enough money, simply skip their turn. Only declare bankruptcy when needing to pay another player.

## My plan and thoughts for solving this problem
1. Load board from the json
2. Represent the players and properties
3. Implement movement logic
4. Implement propery purchase
5. Implement rent logic
6. Add monopoly rule
7. Add bankruptcy condition
8. Simulate game loop