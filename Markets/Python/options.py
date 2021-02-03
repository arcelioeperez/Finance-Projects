"""
P/L -- profit/loss 
Calls (break_even and P/L)
Puts (break_even and P/L) 

Options are made up of: 
- Intrinsic Value 
- Extrinsic Value 

Add the shebang (first line): 
!/usr/bin/env python3
Make it executable: 
chmod +x options.py 
Run it with: 
./options.py 

Variables: 
S - current price
K - strike price
cprice - call contract price 
pprice - put contract price
call_be - break even call 
put_be - break even put
"""
class Options: 
    def __init__(self, S, K):
        self.S = S
        self.K = K
    def call_be(self, cprice):
        self.call_be = self.K + cprice
        return self.call_be
    def put_be(self, pprice): 
        self.put_be = self.K - pprice
        return self.put_be
    def call(self, end):
        profitability = []
        prices = []
        for i in range(self.S, end+5, 5): 
            prices.append(i) 
            profitability.append(round(max(0, i - self.call_be), 2))
        ans = zip(prices, profitability) 
        print("P/L Call Options")
        for i,j in ans:
            print(i, j)
        #return print(f"P/L Call Option: ", *zip(prices, profitability))
    def put(self, end): 
        profitability = []
        prices = []
        for i in range(self.S, end+5, 5): 
            prices.append(i)
            profitability.append(round(max(0, self.put_be - i)))
        ans = zip(prices, profitability) 
        print("P/L Put Options")
        for i,j in ans: 
            print(i, j)
        #return print(f"P/L Put Option: ", *zip(prices, profitability)) 

# Tests 
current_price = 110 
strike_price = 90

#creating an object -- test
test = Options(current_price, strike_price)

#cprice -- contract price per contract (each contract 100 shares)
cprice = 1.20 

#end value for the loop 
end_value = 150 

#answers
print("Break Even: ", test.call_be(cprice)) 
test.call(end_value) 
