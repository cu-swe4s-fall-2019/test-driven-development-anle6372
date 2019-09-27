"""Function for reading data from stdin to list

Parameters
----------
col_num : the number of the column of data to be read from standard in

Returns
-------
V : List of data in the specified column from standard in
"""
import sys
import select


# Function for importing some data from standard in
def read_stdin_col(col_num):

    # Checks input data to ensure valid types
    if col_num is None:
        return None
    if isinstance(col_num, bool):
        raise TypeError('Input must be integer')
        return None
    if not isinstance(col_num, int):
        raise TypeError('Input must be integer')
        return None

    if select.select([sys.stdin, ], [], [], 0.0)[0]:
        V = []
        for l in sys.stdin:
            A = [int(x) for x in l.split()]
            V.append(A[int(col_num)])
        return V
    return col_num
