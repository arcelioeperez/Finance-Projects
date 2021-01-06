"""
Monte Carlo Simulation - Black Scholes Merton Differential Equation
Example is of a Put Option 
The Black Scholes Merton model only applies to European Options

From the book: Python for Finance -Yves Hilpisch (page 300)

***The code was modified to use OOP - it originally was a function***

Variables: 
M: intervals 
I: paths 

S0: value of the option by  time
sigma: constant of instantaneous volatility
T: time horizon of the simulation - maturity date
dt: T/M
r: riskless, short-term rate
z = rn = brownian motion

Run with (GNU-Linux and MacOS): 
python3 monte_carlo.py

More references: 
Black-Scholes-Merton SDE (geometric Brownian Motion) 
dSt = r*St*dt + sigma*St*dZt 

(The equation presented here is the Black-Scholes-Merton differential equation)
St = St - dt exp((r - sigma**2/2) dt + dt*sqrt(dt*Z))

***More information here***
Book: https://learning.oreilly.com/library/view/python-for-finance/9781491945360/
Black Sholes Merton: https://maths.ucd.ie/courses/mst3024/section4-3.pdf
Euler Methods (MIT): https://web.mit.edu/10.001/Web/Course_Notes/Differential_Equations_Notes/node3.html
"""

import numpy as np 
import math
import matplotlib.pyplot as plt

class MonteCarlo: 
    def __init__(self, M, I): 
        self.M = M
        self.I = I
        self.T = 1.0 
        self.S0 = 36 
        self.r = 0.06 
        self.sigma = 0.02 
        self.dt = self.T / self.M 
        self.S = np.zeros((self.M + 1, self.I))
    def get_s(self): 
        self.S[0] = self.S0 
        rn = np.random.standard_normal(self.S.shape)
        #Euler scheme 
        for t in range(1, self.M + 1):
            self.S[t] = self.S[t-1] * np.exp((self.r - self.sigma ** 2 / 2)
                    * self.dt + self.sigma * math.sqrt(self.dt) * rn[t])
        return self.S 
    def mean_end(self): 
        return self.S[-1].mean()
    def end_value(self): 
        return self.S0 * math.exp(self.r * self.T)
    def estimator(self, K): 
        self.K = K 
        C = math.exp(-self.r * self.T) * np.maximum(self.K - self.S[-1], 0).mean()
        return C
    def plotter(self):
        end = []
        for i in self.S: 
           #plt.hist(MonteCarlo.get_s(self), bins = 3)
            end.append(i[-1])
        plt.plot(end)
        plt.title("Simulated End-Of-Period Values - i.e. S[-1]")
        return plt.show()
    
"""
------------------
Tests
------------------
for i in S.get_s():
    print(i[-1])

end = []
for i in S.get_s(): 
    end.append(i[-1]) 

plt.plot(end)
plt.show()

end = []
for i in S.get_s(): 
    for j in i:
        end.append(j) 

plt.plot(end[-11:-1])
plt.show()

-----------------------
i[-1] takes the end of each list
----------------------
a = [[2,4,6], [3,5,2], [3,5,8]]
for i in a: 
    print(i[-1])
"""
#Creating an object
#M - intevals
#S - number of paths 


M = 10
I = 500
#Creates the 'S' object with interval 10 and number of paths 500
S = MonteCarlo(M, I)
print("S = ", S.get_s())
print("Mean End-Of-Period Value: ", S.mean_end())
print("Expected End-Of-Period Value: ", S.end_value()) 
print("C (estimator) for the put option with strike-price of K = 40: ",S.estimator(K = 40))
#Calls the plotter method - plots the end of period values
S.plotter()
