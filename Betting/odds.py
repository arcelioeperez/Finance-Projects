"""
Profit when Betting

Example from the book: Mathematics for Finance by Donald G. Sarri 

Odds 
Game: Vikings - Packers

Bob 25-1 (Vikings win) 

Sue 1.20-1 (Packers win)

Assumptions: 
- Money to bet: $100.00
    x: amount to bet on the Packers
    100 - x: amount to bet on the Vikings 


If Packers win: 
25x - (100 - x) --> 26x - 100
solving x: 
    x = 3.85

If Vikings win: 
1.20(100 - x) - x --> 2.20x = 120
solving x: 
    x = 54.55

3.85 < x < 54.55


x = Symbol('x')
a = solve(x*2.20 - 120, x)
type(a) is a list with the answer of the equation 


Links: 
https://pythonforundergradengineers.com/sympy-two-equations-for-two-unknows-and-statics-problem.html

https://www.google.com/search?channel=fs&client=ubuntu&q=sympy
"""

from sympy.solvers import solve
from sympy import Symbol
import math 

class Bets: 
    def __init__(self, principal, o1, o2): 
        self.principal = principal
        self.o1 = o1 
        self.o2 = o2
    def solution(self, option1 = None, option2=None):
        if option1 == True and option2 == None:
            x = Symbol('x')
            solution = solve(x*self.o1 - (self.principal - x), x) 
        elif option1 == None and option2 == True: 
            x = Symbol('x') 
            solution = solve(self.o2*(self.principal - x) - x,x)
        else: 
            print("Error")
        return solution 
    def solution_o1(self): 
        x = Symbol('x')
        self.sol_o1 = solve(self.o1*x - (self.principal - x), x)
        for i in self.sol_o1: 
            self.sol_o1 = float(i)
        return self.sol_o1
    def solution_o2(self): 
        x = Symbol('x')
        self.sol_o2 = solve(self.o2 * (self.principal - x) - x, x) 
        for i in self.sol_o2: 
            self.sol_o2 = i
        return self.sol_o2
    def try_o1(self): 
        res = []
        ind = []
        for i in range(math.floor(self.sol_o1),math.floor(self.sol_o2), 5): 
            eq = self.o1 * i - self.principal 
            res.append(eq) 
            ind.append(i) 
        ans = zip(ind, res)
        return ans

# Test 
test = Bets(principal = 100, o1 = 25, o2 = 1.20)
#print(test.solution(option1 = None, option2 = True))
test.solution_o1() 
test.solution_o2()

print(*test.try_o1())  
