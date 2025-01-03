# Extended Euclidean Algorithm using Sriram's algorithm.


def gcd(m, n):
    '''Computes the gcd of two numbers and returns gcd as an integer, along with Bézout coefficients as a tuple.'''

    (s1, t1) = (1, 0)  # Initial values for the Bézout coefficients of m
    (s2, t2) = (0, 1)  # Initial values for the Bézout coefficients of n

    while (n > 0):
        # Run until m % n = 0
        k = m % n  # First step in the Euclidean algorithm: remainder of m divided by n
        q = m // n  # Integer division to record quotient (used in Bézout coefficient update)

        m = n  # Set m to the value of n (for next cycle of algorithm)
        n = k  # Set n to the remainder k (for next cycle of algorithm)

        (s2_hat, t2_hat) = ((s1 - q * s2), (t1 - q * t2))  # Update s2, t2 using the recurrence relation

        (s1, t1) = (s2, t2)  # Set the new s1, t1 for next cycle
        (s2, t2) = (s2_hat, t2_hat)  # Set the new s2, t2 for next
    
    return m, (s1, t1) # The final value of m is the gcd, and s1, t1 are the Bézout coefficients


#Tests

print(gcd(198, 21))

