# Imports
from sympy import isprime


# Main Function Code Feature for RSA

# ----------------------HELPER FUNCTIONS----------------------
def FME(b, n, m):
    '''Calculates the mod of numbers with large exponents. Accepts integers in format b^n mod m, returns integer.'''
    result = 1
    square = b % m # Initially, square is b mod m

    while n > 0:
        if n % 2 == 1: # If the least significant bit is 1
            result = (result * square) % m # Update result with current square
        square = (square ** 2) % m # Square the base
        n //= 2 # Divide n by 2 (shifting right in binary)
    
    return result

def Euclidean_Alg(a, b):
    '''Computes the gcd of two numbers (Sriram's Algo) and returns gcd as an integer.'''

    while (b > 0):
        # Run until a % b = 0
        k = a % b  
        # Set a, b respectively for next iteration
        a = b 
        b = k 
    
    return a # The final value of a is the gcd

def EEA(a, b):
    '''Computes the gcd of two numbers (Sriram's Algo) and returns gcd as an integer, along with Bézout coefficients as a tuple.'''

    (s1, t1) = (1, 0)  # Initial values for the Bézout coefficients of a
    (s2, t2) = (0, 1)  # Initial values for the Bézout coefficients of b

    while (b > 0):
        # Run until a % b = 0
        k = a % b  
        q = a // b  
        # Set a, b respectively for next iteration
        a = b 
        b = k  
        # Update s1, s2, t1, t2 using the recurrence relation
        s1, s2 = s2, s1 - q * s2
        t1, t2 = t2, t1 - q * t2
    
    return a, s1, t1 # The final value of a is the gcd, and s1, t1 are the Bézout coefficients

def Convert_Text(_string):
    '''Accpets a string and returns the corresponding list of integers (ascii).'''
    integer_list = []
    # Iterate through each character in string and record ascii integers in list
    for char in _string:
        integer_list.append(ord(char))
        
    return integer_list

def Convert_Num(_list):
    '''Converts a list of numbers into string of corresponding ascii characters.'''
    _string = ''
    for num in _list:
        _string += chr(num)

    return _string

def factorize(n):
    '''Improved brute forcer of factorization of n.'''
    for i in range(2, int((n ** 0.5) + 1)):
        # We know we only need to iterate until root(n) since we know p or q must be less.
        if n % i == 0 and isprime(i) and isprime(n // i):
            # Check to see if i is a factor AND both factors are prime
            return (n // i, i)
    return False

def parse_to_list(usr_string):
    '''Cleans and converts a list entered as type string into a genuine list.'''
    staged_string = usr_string.strip("[]").split(",") # Remove brackets and create list of strings
    
    return_lst = []
    for element in staged_string:
        # Append each cleaned element as an integer to the return list
        return_lst.append(int(element.strip("' ")))

    return return_lst


# ----------------------OPERATOR FUNCTIONS----------------------

def Find_Public_Key_e(p, q):
    '''Generates a public key based on two large primes'''
    # Compute values n, k and set an initial e.
    n = p * q
    k = (p - 1) * (q - 1)
    e = 13 # Set an initial prime for e (will most likely change)

    # Find e such that 1 < e < 90000 and GCD(e, k) == 1 (relatively prime)
    while Euclidean_Alg(k, e) != 1:
        e += 2  # Start from 2 to avoid e == 1

    return n, e

def Find_Private_Key_d(e, p, q):
    '''Finds a private key based on two large primes and e.'''
    # Calculate k
    k = (p - 1) * (q - 1)
    # Find the Bézout Coefficients, s1 is our inverse of e mod k
    a, s1, s2 = EEA(e, k) 
    # We know that d = s1
    # The modular inverse of e mod k is s1 (from Bézout coefficients)
    d = s1 % k  # Ensure d is positive by taking it mod k
    
    return d

def Encode(n, e, message):
    '''Encodes a message using RSA. Accepts n, e, message as a string and returns list of integers.'''
    cipher_text = []
    integer_list = Convert_Text(message)

    for number in integer_list:
        # Append each encoding calculation (using fast mod exponentiation) to cipher
        cipher_text.append(FME(number, e, n))

    return cipher_text

def Decode(n, d, cipher_text):
    '''Decodes a message using RSA. Accepts n, d, list of integers and returns a string.'''
    integer_list = []

    for number in cipher_text:
        # Append each decoding calculation (using fast mod exponentiation) to integer list
        integer_list.append(FME(number, d, n))

    message = Convert_Num(integer_list)

    return message

def break_code(n, e):
    '''Attempts to break RSA public key encryption. Accepts n, e and returns d'''
    p, q = factorize(n) # Unpack primes into p, q
    d = Find_Private_Key_d(e, p, q) # Calculate d based on found primes

    return d


# ----------------------MAIN----------------------

def main():
    user_input = None
    while user_input != -1: # Set exit sentinal value to -1
        # Begin main program loop
        user_input = input("--------------------------\nWhat would you like to do?\n(a) Generate a public key\n(b) Generate a private key\n(c) Encode a message\n(d) Decode a message\n(e) RSA code break\n(f) Exit Program\n\n Enter a letter: ")
        
        # Handle case unspecified input
        if user_input not in ["a", "b", "c", "d", "e", "f"]:
            print("Unspecified input. Please enter a letter value a through f.")

        # Exit
        if user_input == "f":
            user_input = -1 # Set the user_input value to the sentinal value

        # Generate public key
        if user_input == "a":
            print("--------------------------")
            # Prompt user for inputs
            p = int(input("Please enter a prime number p: ")) # Make sure to convert to int
            q = int(input("Please enter a prime number q: "))
            # Public key calculation (returns tuple)
            pub_key = Find_Public_Key_e(p, q)
            # Return values to user as a touple
            print(f"\nYour public key n, e is {pub_key}")

        # Generate private key
        if user_input == "b":
            print("--------------------------")
            # Prompt user for inputs
            p = int(input("Please enter a prime number p: "))
            q = int(input("Please enter a prime number q: "))
            # Calculate further needed inputs
            n, e = Find_Public_Key_e(p, q)
            # Private key calculation
            d = Find_Private_Key_d(e, p, q)
            # Return value to user 
            print(f"\nYour private key d is {d}")

        # Encode
        if user_input == "c":
            print("--------------------------")
            # Prompt user for inputs
            message_user_encode = input("Please enter the message you'd like to encode: ")
            n = int(input("Please enter a value for n: ")) # Make sure to convert to int
            e = int(input("Please enter your public key, e: "))
            # Encode calculation
            encoded_message = Encode(n, e, message_user_encode)
            # Return encoded message to user
            print(f"\nYour encoded message is {encoded_message}")

        # Decode
        if user_input == "d":
            print("--------------------------")
            # Prompt user for inputs
            message_user = input("Please enter the message you'd like to decode: ")
            n = int(input("Please enter a value for n: "))
            d = int(input("Please enter your private key d: "))
            # Parse message to list of integers (processing)
            message_user_parsed = parse_to_list(message_user)
            # Decode calculation using parsed data
            decoded_message = Decode(n, d, message_user_parsed)
            # Return decoded message to user
            print("\nYour decoded message is: " + decoded_message)

        # Code Break
        if user_input == "e":
            print("--------------------------")
            # Prompt user for inputs
            n = int(input("Please enter a value for n: "))
            e = int(input("Please enter a value for e: "))
            # Private key calculation
            d = break_code(n, e)
            # Return found private key to user
            print(f"\nThe private key d is {d}")



if __name__ == "__main__":
    main()
