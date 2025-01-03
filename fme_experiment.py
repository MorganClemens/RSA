# Doc to test the relative speed of FME against other methods
import cProfile
import re
from fast_modular_exponentation import fast_mod



def NOT_FME(a, n, b):
    '''Manually calculates the modular exponent. Accepts a^n mod b'''
    return (a ** n) % b


def pow_FME(a, n, b):
    '''Utilizes built in pow function which is FME. Accepts a^n mod b'''
    return pow(a, n) % b


# Testing values
a = 6500000
n = 56733
b = 27


# TESTS (time)

# Test for NOT_FME
cProfile.run('NOT_FME(a, n, b)')

# Test for pow_FME
cProfile.run('pow_FME(a, n ,b)')

# Test for fast_mod (my algo)
cProfile.run('fast_mod(a, n, b)')

