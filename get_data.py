
def read_stdin_col(col_num):
    if col_num is None:
        return None
    if isinstance(col_num, bool):
        raise TypeError('Input must be integer')
        return None
    if not isinstance(col_num, int):
        raise TypeError('Input must be integer')
        return None
