import sys
import math


def list_mean(X):
    if X is None:
        return None
    if len(X) == 0:
        return None
    if not isinstance(X, list):
        raise TypeError('Input must be list')
    s = 0
    for l in X:
        if not isinstance(l, int) and not isinstance(l, float):
            raise ValueError('Invalid type in list.')
        s += l
    return s / len(X)



def list_stdev(X):
    if X is None:
        return None
    if len(X) == 0:
        return None
    if not isinstance(X, list):
        raise TypeError('Input must be list')
    s = 0
    for l in X:
        if not isinstance(l, int) and not isinstance(l, float):
            raise ValueError('Invalid type in list.')
        s += l
    return math.sqrt(sum([((s/len(X))-x)**2 for x in X]) / len(X))
