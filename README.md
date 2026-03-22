# Pronto-Monopoly
Hi, this is my repository for the monopoly coding test :)


# Key rules identified (MUST HAVES AND REMEMBER!!!)
- 4 players in a fixed order
- Each player starts with 16 dollars
- Passing GO square gives 1 dollar
- Players are reqquired to purchase any property they land on. Traditional Monopoly mechanics such as auctions or declining purchases are not implemented
- Rent doubles if full colour set is owned
- Game ends when ANY player is bankrupt

## Assumptions
- Players can go into negative money before bankruptcy is triggered
- No skipping purchases or auctioning (this one is implied as there is not other option either buy or don't)
- No other Monopoly rules

## My plan and thoughts for solving this problem
1. Load board from the json
2. Represent the players and properties
3. Implement movement logic
4. Implement propery purchase
5. Implement rent logic
6. Add monopoly rule
7. Add bankruptcy condition
8. Simulate game loop