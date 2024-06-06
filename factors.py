#Converts a future value (f) to a present value (p) using a discount rate (i) and the number of periods (n).
def f_to_p(i, n, f):
    factor = 1 / (1 + i) ** n  
    return f * factor  

#Converts an annuity value (a) to a present value (p) using a discount rate (i), growth rate (j), and number of periods (n).
def a_to_p(i, j, n, a):   
    if i == j:
        factor = n / (1 + i) 
    else:
        factor = (1 - (((1 + j) ** n) * ((1 + i) ** -n))) / (i - j)  
        
    return a * factor 

#Converts a present value (p) to an annuity value (a) using a discount rate (i) and the number of periods (n).
def p_to_a(i, n, p):
    factor = (i * ((1 + i) ** n)) / (((1 + i) ** n) - 1)
    return p * factor  

#Converts a present value (p) to a future value (f) using a discount rate (i) and the number of periods (n).
def p_to_f(i, n, p): 
    factor = (1 + i) ** n 
    return p * factor  
