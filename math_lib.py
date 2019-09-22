import sys
import math

try:
    def list_mean(X):
        return sum(X)/len(X)
except ZeroDivisionError:
    print('List is empty')
    sys.exit(1)

try:
    def list_stdev(X):
        return math.sqrt(sum([((sum(X)/len(X))-x)**2 for x in X]) / len(X))
except ZeroDivisionError:
    print('List is empty')
    sys.exit(1)