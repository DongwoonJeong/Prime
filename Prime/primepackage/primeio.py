#!/usr/bin/python

"""
Init module that import modules.
"""

__author__ = "Dongwoon Jeong"
__license__ = "VSU"
__version__ = "0.1"
__email__ = "dwjeong@valdosta.edu"
__status__ = "Individual project"

import csv


def write_primes(list_l, file_name):
    """the function read a list of prime numbers and a csv file name as parameters,
     write the number in the list to the csv file
    '''Summary line.
     Args:
        file_name (str): input file name.
        list_l (int): input list.
     Returns:
        file: output file.
     Raises:
        IOError: io error.
     Examples:
        >>> write_primes(prime, 'output.csv')
    '''
    """
    try:
        file_writer = open(file_name, 'w')
        csv_writer = csv.writer(file_writer)
        csv_writer.writerows([list_l])
    except IOError as argument:
        print("Error: can not write file", argument)
    else:
        print("Successfully wrote contents in the file ")
    finally:
        file_writer.close()


def read_primes(file_name):
    """the function read a csv file name as the parameter,
    read the primes numbers saved in the csv file,
    save them into a list, return the list
    '''Summary line.
    Args:
        file_name (str): input file name.
    Returns:
        list: a list of strings from input file.
    Raises:
        IOError: io error.
    Examples:
        >>> li_st = read_primes('output.csv')
        >>> print(li_st)
    '''
    """

    list1 = []
    try:
        file_reader = open(file_name, 'r')
        text = csv.reader(file_reader)
    except IOError as argument:
        print("Error: can not find file or read data", argument)
    else:
        for line in text:
            list1.append(line)
            return list1
