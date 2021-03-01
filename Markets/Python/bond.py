"""
Bond prices

source: Mastering Python for Finance by James Ma Weiming
"""
import scipy.optimize as optimize

def bond_ytm(price, par, T, coup, freq = 2, guess = 0.05):
    freq = float(freq)
    periods = T * freq
    coupon = coup/100.*par/freq

    dt = []
    for i in range(int(periods)):
        ans = (i+1)/freq
        dt.append(ans)

    ytm_function = lambda y: \
        sum([coupon / (1+y/freq) ** (freq*t) for t in dt]) + par/(1+y/freq) ** (freq*t) - price

    return optimize.newton(ytm_function, guess)

a = bond_ytm(95.0428, 100, 1.5, 5.75, 2)
print(a) 
