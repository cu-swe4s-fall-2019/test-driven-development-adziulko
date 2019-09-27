import sys

def read_stdin_col(col_num):
    ''' Read in column number from stdin.

    Parameters
    ----------
    col_num :
        integer specifying column

    Returns
    ----------
    col :
        Array of column data
    '''

    if col_num is None:
        return None
    if len(col_num) == 0:
        return None

    col = []

    for line in sys.stdin:
        A = line.rstrip().split()
        col.append(int(A[col_num]))
    return col
