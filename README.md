![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg) 

# Finance Projects    

**Monte Carlo Simulation - Black-Scholes-Merton Put Option (European Option)**        

![image](MonteCarlo/monte_carlo_plot.png)   

**Compound Interest Formula - Code in C++**    

### A = Pe<sup>rt</sup>  

This program uses references and vectors instead of pointers and arrays --
initially it was done this way (using pointers and arrays), but I decided to change it to make it more
compatible with C++.  

Using arrays and pointers is allowed in C++, but it is more of
a C implementation.  

**Where:**     
A = end amount    
P = principal amount    
e = Euler constant   
r = rate of growth   
t = time period    

```python
#compile
g++ compound_interest.cpp -o ci

#run 
./ci 
```  

**Compound Interest - C**    

Uses pointers and arrays.  

```python 
#compile
gcc compound_interest.c -lm 

#run 
./a.out
```

**Citation:**   
Python for Finance - Yves Hilpisch - [O'reilly Books]( https://learning.oreilly.com/library/view/python-for-finance/9781491945360/)  
Black-Scholes-Merton - [UCD](https://maths.ucd.ie/courses/mst3024/section4-3.pdf)  
Euler Methods - [MIT](https://web.mit.edu/10.001/Web/Course_Notes/Differential_Equations_Notes/node3.html)  
