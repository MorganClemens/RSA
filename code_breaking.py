
import cProfile
import re

def factorize(n):
    '''Attempts to Brute force the factors of a given integer. Accepts integers, returns an integer.'''
    for i in range(2, n - 1):
        # Iterate over range 2 to n -1
        if n % i == 0:
            # Check to see whether i divides n
            return i
    return False

cProfile.run('print(factorize(56853839))') # Run the function within as a string to get measurements



print(56853839 % 7 == 0)