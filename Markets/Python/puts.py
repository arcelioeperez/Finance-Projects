"""
Put Options Profitability

Variables: 
S = current price 
E = strike price

Puts = max(0, (E - contract_price) - S) 

The Profitability is in a **per share basis** 
"""

def put_profitability(S, E, contract_price): 
    profitability = max(0, (E - contract_price) - S) 
    return profitability 

S = 90 
E = 100 
contract_price = 2 

test = put_profitability(90, 100, 2) 
print("Profitability: ", test) 
