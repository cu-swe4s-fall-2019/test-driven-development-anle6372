import sys
import select

def read_stdin_col(col_num):


    if col_num is None:
        return None
    if isinstance(col_num, bool):
        raise TypeError('Input must be integer')
        return None
    if not isinstance(col_num, int):
        raise TypeError('Input must be integer')
        return None

    if select.select([sys.stdin,],[],[],0.0)[0]:
        V = []
        for l in sys.stdin:
            A = [int(x) for x in l.split()]
            V.append(A[int(col_num)])
        print(V)
    return col_num