#!/usr/bin/python
"""
A module that calculate if its prime number,
get numbers of prime numbers according to the input.
"""

__author__ = "Dongwoon Jeong"
__license__ = "VSU"
__version__ = "0.1"
__email__ = "dwjeong@valdosta.edu"
__status__ = "Individual project"


def is_prime(num_a):
    """read a natural number, return True if it is a prime number,
     return False otherwise
    '''Summary line.

    Extended description.

    Args:
        num_a(int): input number

    Returns:
        Boolean: if the number is prime or not.

    Raises:
        IOError: io error.

    Examples:
        >>> if is_prime(3);

    '''
    """
    if num_a < 2:
        return False
    for i in range(2, num_a):
        if num_a % i == 0:
            return False
    return True


def get_prime(num_b):
    """read an integer number parameter, return a list containing prime numbers,
    the number of prime numbers in the list is specified by the function parameter
    '''Summary line.

    Extended description.

    Args:
        num_b(int): input file name.

    Returns:
        list: a list of strings.

    Raises:
        IOError: io error.

    Examples:
        >>> primes = get_prime(100)

    '''
    """
    prime = []
    num = 0
    count = 0
    while count < num_b:
        if is_prime(num):
            prime.append(num)
            count += 1
        num += 1
    return prime
