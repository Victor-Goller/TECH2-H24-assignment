"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""
from math import sqrt
import numpy as np

def std_loops(x):
    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    x = [1,2,3,4,5]

    sum_i = 0
    squ = 0
    n = 5

    for i in range(1,6):
        sum_i = sum_i + i
        squ = squ + i**2
    
    var = squ/n - (sum_i/n)**2

    sd = sqrt(var)
print("Using loops:")
print(f"The deviation is equal to: {sd}\n")


def std_builtin(x):
    """
    Compute standard deviation of x using the built-in functions sum()
    and len().

    Parameters
    ----------
    num_lst: Sequence of numbers

    Returns
    -------
    deviation : float
        Standard deviation of the list of numbers.
    """
    num_lst_squ = [1**2, 2**2, 3**2, 4**2, 5**2]

    mean_ = sum(num_lst)/len(num_lst)
    squ_ = sum(num_lst_squ)/len(num_lst_squ)
    variance = squ_ - mean_**2
    deviation = sqrt(variance)
print("Using built-in functions sum() and len():")
print(f"The deviation is equal to: {deviation}\n")



"""
Compute standard deviation of num_lst using NumPy.
    
Parameters
----------
num_lst: Sequence of numbers
Returns

-------
deviation_ : float
    Standard deviation of the list of numbers.
"""

deviation_ = np.std(num_lst)
print("Using NumPy:")
print(f"The deviation is equal to: {deviation_}\n")


if __name__ == '__main__':
    pass
