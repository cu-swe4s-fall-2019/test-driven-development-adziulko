import sys
import math


def list_mean(L):
    '''Compute the mean of an array. Expects a non-empty array.

    Parameters
    ----------
    L : list of int
        array containing numbers whose mean is desired.

    Returns
    -------
    m
        Arithmetic mean of the values in V

    '''
    if L is None:
        return None
    if len(L) == 0:
        return None

    s = 0

    for line in L:
        s += line



    m = sum(L)/len(L)
    return m




def list_stdev(L):
    '''Compute the standard deviation of an array. Expects a non-empty array.

    Parameters
    ----------
    L : list of int
        Non-empty array containing numbers whose standard deviation is desired.

    Returns
    -------
    sd
        Standard deviation of the values in V

'''
    if L is None:
        return None
    if len(L) == 0:
        return None
    else:
        mean = list_mean(L)



    sd = math.sqrt(sum([(mean-x)**2 for x in L]) / len(L))
    return sd
