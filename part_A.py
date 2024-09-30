from math import sqrt
import numpy as np

def std_loops(x, start, end):
    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    x : Sequence of numbers
    start : int
        Start index for the interval.
    end : int
        End index for the interval.

    Returns
    -------
    sd : float
        Standard deviation of the numbers in the interval.
    """
    interval = x[start:end]
    n = 5                      # we know that the lengt of the interval is 5
    sum_i = 0
    squ = 0

    for i in interval:
        sum_i = sum_i + i
        squ = squ + i**2
    
    mean_i = sum_i / n
    mean_squ = squ / n
    var = mean_squ - mean_i**2
    sd = sqrt(var)
    
    return sd


def std_builtin(x, start, end):
    """
    Compute standard deviation of x using built-in functions sum() and len().

    Parameters
    ----------
    x : Sequence of numbers
    start : int
        Start index for the interval.
    end : int
        End index for the interval.

    Returns
    -------
    sd : float
        Standard deviation of the numbers in the interval.
    """
    interval = x[start:end]
    n = len(interval)
    sum_i = sum(interval)
    squ = sum([i**2 for i in interval])

    mean_i = sum_i / n
    mean_squ = squ / n
    var = mean_squ - mean_i**2
    sd = sqrt(var)
    
    return sd


def std_numpy(x, start, end):
    """
    Compute standard deviation of x using NumPy.

    Parameters
    ----------
    x : Sequence of numbers
    start : int
        Start index for the interval.
    end : int
        End index for the interval.

    Returns
    -------
    sd : float
        Standard deviation of the numbers in the interval.
    """
    interval = np.array(x[start:end])
    return np.std(interval)


if __name__ == '__main__':
    
    # Our list
    x = [1, 2, 3, 4, 5]

    # Set the interval
    start = 0
    end = len(x)

    # Using loops
    sd_loops = std_loops(x, start, end)
    print("Using loops:")
    print(f"The deviation is equal to: {sd_loops}\n")

    # Using built-in functions
    sd_builtin = std_builtin(x, start, end)
    print("Using built-in functions sum() and len():")
    print(f"The deviation is equal to: {sd_builtin}\n")

    # Using NumPy
    sd_numpy = std_numpy(x, start, end)
    print("Using NumPy:")
    print(f"The deviation is equal to: {sd_numpy}\n")
