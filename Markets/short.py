"""
Short Selling Script

Price of the underlying stock goes up: 
- Margin call 

Price goes down: **to do** 
- Money to the seller's account
"""

import pandas as pd

class Short: 
    def __init__(self, shares, price, mfee=0.3): 
        self.shares = shares
        self.price = price
        self.mfee = mfee 
    def price_increase(self, end, steps=5):
        self.end = end 
        self.steps = steps
        principal = self.shares * self.price
        margin_amount = 0.5 * principal 
        initial_req = margin_amount + principal 
        short_value = 0
        margin_call = 0
        total_req = 0
     
        data = pd.DataFrame([]) 

        for i in range(self.price + self.steps, self.end, self.steps): 
            short_value = self.shares * i 
            margin_req = short_value * self.mfee
            total_req = short_value + margin_req
            if total_req < initial_req: 
                margin_call = 0
                data = data.append(pd.DataFrame({"Shares": [self.shares],
                    "Share Price": [i], 
                "Short Sale Value": [short_value], "Maintenance Margin":
                [margin_req], "Total Req": [total_req], "Margin Call":
                [margin_call]}), ignore_index = True ) 
            else: 
                margin_call = total_req - initial_req
                data = data.append(pd.DataFrame({"Shares": [self.shares],
                    "Share Price": [i], 
                "Short Sale Value": [short_value], "Maintenance Margin":
                [margin_req], "Total Req": [total_req], "Margin Call":
                [margin_call]}), ignore_index = True ) 

        print(data) 
# Test
test = Short(shares = 1000, price = 50,  mfee = 0.3) 
ans = test.price_increase(end = 80, steps = 5)
print(ans)     
