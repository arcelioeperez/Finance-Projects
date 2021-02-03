"""
MIT License

Copyright (c) 2021 Arcelio E. Perez Garcia

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Short Selling Script

Price of the underlying stock goes up: 
- Margin call 

Price goes down:  
- Money to the short seller's account


first_transaction: 
prints out the first transaction of the short position

price_increase: 
prints out the all the margin values and the margin calls for the short seller

price_decrease: 
prints out the money going to the short seller's account
"""

import pandas as pd

class Short: 
    def __init__(self, shares, price, mfee=0.3): 
        self.shares = shares
        self.price = price
        self.mfee = mfee 
    def first_transaction(self): 
        principal = self.shares * self.price
        margin_amount = 0.5 * principal 
        total_req = principal + margin_amount 
        ft = pd.DataFrame({"Shares": [self.shares],
                    "Share Price": [self.price], 
                    "Short Value": [principal], "Initial Margin":
                    [margin_amount], "Total Margin": [total_req]})

        print(ft) 
    def price_increase(self, end, steps=5):
        principal = self.shares * self.price
        margin_amount = 0.5 * principal 
        initial_req = margin_amount + principal 
        short_value = 0
        margin_call = 0
        total_req = 0
     
        data = pd.DataFrame([]) 

        for i in range(self.price + steps, end, steps): 
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

    def price_decrease(self, end, steps= 5):
        principal = self.shares * self.price 
        margin_req = 0.5 * principal 
        initial_req = principal + margin_req
          
        data = pd.DataFrame([])
        for i in range(self.price - steps, end, -steps): 
            short_value = self.shares * i 
            margin_req = short_value * 0.5
            total_req = short_value + margin_req
            mar_released = initial_req - total_req

            data = data.append(pd.DataFrame({"Shares": [self.shares],
                "Share Price": [i], 
            "Short Sale Value": [short_value], "Additional Margin":
            [margin_req], "Total Req": [total_req], "Margin Released":
            [mar_released]}), ignore_index = True)

        print(data)



# Test
test = Short(shares = 1000, price = 50,  mfee = 0.3) 
test.first_transaction()
test.price_increase(end = 80, steps = 5)
test.price_decrease(end = 25, steps = 5)


print("###################################")

# Test 2
test2 = Short(shares = 1000, price = 25, mfee = 0.3) 
test2.first_transaction() 

test2.price_increase(end = 50, steps = 10)
test2.price_decrease(end = 5, steps = 5) 

print("####################################")
print("END OF SCRIPT")
