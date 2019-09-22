import sys
import math


def list_mean(X):
    if X is None:
        return None
    if len(X) == 0:
        return None
    return sum(X) / len(X)


def list_stdev(X):
    if X is None:
        return None
    if len(X) == 0:
        return None
    return math.sqrt(sum([((sum(X)/len(X))-x)**2 for x in X]) / len(X))
