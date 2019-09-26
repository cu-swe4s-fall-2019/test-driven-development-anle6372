import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import math_lib


def boxplot(L, out_file_name):


    if L is None:
        return None
    if len(L) == 0:
        return None
    if not isinstance(L, list):
        raise TypeError('Input must be list')
    s = 0
    for l in L:
        if not isinstance(l, int) and not isinstance(l, float):
            raise ValueError('Invalid type in list.')

    out_file = out_file_name
    plt.title('mean: ' + str(math_lib.list_mean(L)) + '  ' + 'stdev: ' + str(math_lib.list_stdev(L)), fontsize=20)
    plt.xlabel('sample')
    plt.ylabel('values')

    plt.boxplot(L)
    plt.savefig(out_file, bbox_inches='tight')

def histogram(L, out_file_name):
    if L is None:
        return None
    if len(L) == 0:
        return None
    if not isinstance(L, list):
        raise TypeError('Input must be list')
    s = 0
    for l in L:
        if not isinstance(l, int) and not isinstance(l, float):
            raise ValueError('Invalid type in list.')

    out_file = out_file_name
    plt.title('mean: ' + str(math_lib.list_mean(L)) + '  ' + 'stdev: ' + str(math_lib.list_stdev(L)), fontsize=20)
    plt.xlabel('frequency')
    plt.ylabel('values')

    plt.hist(L)
    plt.savefig(out_file, bbox_inches='tight')

def combo(L, out_file_name):
    if L is None:
        return None
    if len(L) == 0:
        return None
    if not isinstance(L, list):
        raise TypeError('Input must be list')
    s = 0
    for l in L:
        if not isinstance(l, int) and not isinstance(l, float):
            raise ValueError('Invalid type in list.')

    out_file = out_file_name
    width = 10
    height = 5
    fig = plt.figure(figsize=(width, height), dpi=300)
    ax = fig.add_subplot(1, 2, 1)
    ax.boxplot(L)
    ax.set_xlabel('sample')
    ax.set_ylabel('values')
    ax = fig.add_subplot(1, 2, 2)
    ax.hist(L)
    ax.set_xlabel('frequency')
    ax.set_ylabel('values')
    fig.suptitle('mean: ' + str(math_lib.list_mean(L)) + '  ' + 'stdev: ' + str(math_lib.list_stdev(L)), fontsize=20)
    plt.savefig(out_file, bbox_inches='tight')
