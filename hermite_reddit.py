
from math import sqrt, exp, pi, factorial  
from numpy import linspace  
from pylab import figure, plot, xlabel, ylabel, legend, show, title  
#from gaussxw import gaussxw

# Recursive formula for the Hermite polynomials (Physicist's, not Probabilist's)  

def Hermite(n, x):  
    if n == 0:    
        return 1    # first polynomial  
    elif n == 1:  
        return 2 * x    # second polynomial  
    else:  
        return 2 * x * Hermite(n-1, x) - 2 * (n - 1) * Hermite(n - 2, x)  

# n-th wavefunction  

def psi(n, x):  
    return (1 / sqrt(2**n * factorial(n) * sqrt(pi))) * exp((- x**2 / 2)) * Hermite(n, x)  

# Plot psi_30(x)  
def main():
    Xp = linspace(-10, 10, 10)  
    PSI30 = []  
    
    for k in range(10):  
        PSI30.append(psi(30, Xp[k]))  
    
    plot(Xp, PSI30)  
    show()  
    
