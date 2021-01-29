"""
Call Options Profitability 

Variables:
S = current price 
E = strike price
contract_price = price for one call contract 

Call = max(0, S - Breakeven) 
Breakeven = E + contract price

The Profitability is in a **per share basis** 
"""
def call_profitability(S, E, contract_price):
    profitability = max(0, S - (E + contract_price)) 
    return profitability 

S = 110 
E = 90 
contract_price = 1.20
test = call_profitability(S, E, contract_price)
print(f"""Profitability with current price: {S}, strike price: {E}, and price per 
contract: {contract_price} = """, round(test, 2)) 
