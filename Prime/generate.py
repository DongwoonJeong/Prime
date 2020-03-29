#!/usr/bin/python
 
"""A Python program generating a list of prime numbers and output them into a csv file
 
"""
 
from primepackage import *


def main():
    """Generate 100 prime numbers and output it into output.csv file
 
    """
    try:
        primes = get_prime(-5)
        write_primes(primes, 'output.csv')
        l = read_primes('output.csv')
        print(l)
    except Exception as err:
        print("Catch error in main")
        raise


if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        print(err.args, err)
