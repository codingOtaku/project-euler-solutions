# Module for prime numbers 

from math import sqrt 

def is_prime(num):
    """Returns True if num is a prime."""
    if num == 2:
        return True
    if num%2 == 0 or num < 2:
        return False

    for i in range(3,int(sqrt(num)+1),2):
        if num%i == 0:
            return False

    return True
