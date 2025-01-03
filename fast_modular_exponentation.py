# A module to compute Fast Modular Exponentiation FME

# I decided to choose Sriram's function for my implementation of FME because I liked the idea of doing
# the computations (finding a^2, a^4 ect) and multiplying and taking the mod of what would ultimately
# be the result in parallel. I also thought the utilization of a while loop fit this application well
# and the implementation of this algorithm the most straightforward. The algorithm's readibility is
# also a big reason I chose to implement this version to make my future debugging journey a little 
# more straightforward. 


def fast_mod(a, n, b):
    '''Calculates the mod of numbers with large exponents. Accepts in format a^n mod b'''
    result = 1
    square = a % b # Initially, square is a mod b

    while n > 0:
        if n % 2 == 1: # If the least significant bit is 1
            result = (result * square) % b # Update result with current square
        square = (square ** 2) % b # Square the base
        n //= 2 # Divide n by 2 (shifting right in binary)
    
    return result


# Testing

print(fast_mod(23, 1002, 41))








