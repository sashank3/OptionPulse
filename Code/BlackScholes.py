# -*- coding: utf-8 -*-
"""

    Calculate the theoretical price of a European call option using the Black-Scholes model.
    
    Parameters:
        S (float): Current price of the underlying asset (stock).
        K (float): Strike price of the option.
        T (float): Time to expiration (in years).
        r (float): Risk-free interest rate (annualized).
        sigma (float): Volatility of the underlying asset's returns.
        
    Returns:
        float: Theoretical price of the European call option.

"""

import numpy as np
from scipy.stats import norm

def black_scholes_european_call(S, K, T, r, sigma):

    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    N_d1 = norm.cdf(d1)
    N_d2 = norm.cdf(d2)
    
    call_price = S * N_d1 - K * np.exp(-r * T) * N_d2
    return call_price

# Example usage
S = 100  # Current stock price
K = 105  # Strike price
T = 0.5  # Time to expiration (in years)
r = 0.05  # Risk-free interest rate
sigma = 0.2  # Volatility

option_price = black_scholes_european_call(S, K, T, r, sigma)
print("Theoretical European Call Option Price:", option_price)
