"""Library for computing the mean and standard deviation of some data

Parameters
----------
X : a list containing only integers and floats

Returns
-------
mean : Arithmetic mean of the values in list X
stdev : The standard deviation of the values in list X
"""


import math


# function for calculating the mean of some data
def list_mean(X):
    # checks invalid inputs
    if X is None:
        return None
    if len(X) == 0:
        return None
    if not isinstance(X, list):
        raise TypeError('Input must be list')
    # calculates mean
    s = 0
    for l in X:
        if not isinstance(l, int) and not isinstance(l, float):
            raise ValueError('Invalid type in list.')
        s += l
    return s / len(X)


# function for calculating the standard deviation of some data
def list_stdev(X):
    # checks invalid inputs
    if X is None:
        return None
    if len(X) == 0:
        return None
    if not isinstance(X, list):
        raise TypeError('Input must be list')
    # calculates mean
    s = 0
    for l in X:
        if not isinstance(l, int) and not isinstance(l, float):
            raise ValueError('Invalid type in list.')
        s += l
    return math.sqrt(sum([((s/len(X))-x)**2 for x in X]) / len(X))
