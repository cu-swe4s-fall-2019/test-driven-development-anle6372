
def boxplot(X, out_file_name):
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

def histogram(X, out_file_name):
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

def combo(X, out_file_name):
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
