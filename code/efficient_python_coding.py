"""
This file contains some Python code demonstrating efficient coding using Python.
Author: CreativeCloudAppDev2020
"""

# Importing necessary libraries


from mpmath import *

mp.pretty = True
from functools import reduce


# Checking whether a string is a number or not


def is_number(string: str) -> bool:
    try:
        mpf(string)
        return True
    except ValueError:
        return False


# 1. Getting the mpf sum of elements in a list


def mpf_sum_of_list(a_list: list) -> mpf:
    return mpf(str(sum(mpf(str(elem)) for elem in a_list if is_number(str(elem)))))


"""
Longer version for #1:

def mpf_sum_of_list(a_list: list) -> mpf:
    sum: mpf = mpf("0")  # initial value
    for elem in a_list:
        if is_number(str(elem)):
            sum += mpf(str(elem))
            
    return sum
"""


# 2. Getting the mpf product of elements in a list


def mpf_product_of_list(a_list: list) -> mpf:
    return mpf(str(reduce(lambda a, b: mpf("1") if (not is_number(str(a)) and not is_number(str(b))) else
                mpf(str(a)) if (is_number(str(a)) and not is_number(str(b))) else
                mpf(str(b)) if (is_number(str(b)) and not is_number(str(a))) else
                mpf(str(a)) * mpf(str(b)), a_list)))


"""
Longer version of #2:

def mpf_product_of_list(a_list: list) -> mpf:
    product: mpf = mpf("1")  # initial value
    for elem in a_list:
        if is_number(str(elem)):
            product *= mpf(str(elem))
            
    return product
"""


# 3. Calculating the factorial of an integer


def factorial(n: int) -> int:
    return 0 if n < 0 else 1 if n == 0 or n == 1 else n * factorial(n - 1)


"""
Longer version for #3:

def factorial(n: int) -> int:
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
"""


# 4. Calculating the nth fibonacci number


def fibonacci(n: int) -> int:
    return 0 if n < 0 else n if n == 0 or n == 1 else fibonacci(n - 1) + fibonacci(n - 2)


"""
Longer version for #4:

def fibonacci(n: int) -> int:
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
"""


# 5. Calculating the number of occurrences of a substring in a string


def count_occurrences(string: str, substring: str) -> int:
    return len(string.split(substring)) - 1


"""
Longer version of #5:

def count_occurrences(string: str, substring: str) -> int:
    count: int = 0  # initial value
    for i in range(0, len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            count += 1
            
    return count
"""
