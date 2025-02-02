# RSA Encryption: Understanding the Code and Math

## Overview
This project is my attempt at a simple implementation of the RSA encryption algorithm, breaking down its key mathematical principles and helper functions. RSA encryption is widely used for secure communication and relies on modular arithmetic, prime factorization, and number theory.

## Features
- Fast Modular Exponentiation for efficient encryption and decryption
- Euclidean Algorithm to compute the Greatest Common Divisor (GCD)
- Extended Euclidean Algorithm for finding the modular inverse
- Prime Factorization function to demonstrate RSA vulnerabilities
- A step-by-step breakdown of how RSA encryption works

## Prerequisites
- Python 3.x

## Usage
Clone this repository and explore the code to experiment with RSA encryption and decryption.

### 1. **Fast Modular Exponentiation (FME)**
```python
 def FME(b, n, m):
     '''Calculates b^n mod m efficiently.'''
     result = 1
     square = b % m

     while n > 0:
         if n % 2 == 1:
             result = (result * square) % m
         square = (square ** 2) % m
         n //= 2
     return result
```
This function is used for modular exponentiation, which is critical in RSA encryption and decryption.

### 2. **Euclidean Algorithm for GCD**
```python
 def Euclidean_Alg(a, b):
     '''Finds the greatest common divisor (GCD) of two numbers.'''
     while b > 0:
         a, b = b, a % b
     return a
```
Ensures that the encryption exponent `e` is valid by confirming it's relatively prime to `(p-1)(q-1)`.

### 3. **Extended Euclidean Algorithm (EEA)**
```python
 def EEA(a, b):
     '''Finds GCD and Bézout coefficients (used for modular inverse).'''
     s1, t1, s2, t2 = 1, 0, 0, 1
     while b > 0:
         k, q = a % b, a // b
         a, b = b, k  
         s1, s2 = s2, s1 - q * s2
         t1, t2 = t2, t1 - q * t2
     return a, s1, t1
```
This function is used to compute the private key `d` as the modular inverse of `e`.

### 4. **Prime Factorization (Breaking RSA)**
```python
 def factorize(n):
     '''Finds prime factors of n.'''
     for i in range(2, int((n ** 0.5) + 1)):
         if n % i == 0 and isprime(i) and isprime(n // i):
             return (n // i, i)
     return False
```
Demonstrates how RSA security depends on the difficulty of prime factorization. I was able to successfully decrypt some of my classmates' messages given enough time.

## Running the Code
To test the RSA functions, run the prototype.py file in your IDE. 

You can modify the values of `p`, `q`, and `e` to experiment with different encryption scenarios.

## License
This implementation of RSA was completed as a personal project and you're welcome to use it for your own projects as well. 

## Author
Morgan Clemens

