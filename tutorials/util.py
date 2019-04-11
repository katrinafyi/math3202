from itertools import product 
from gurobipy import tupledict

def get_elem(matrix, indexes):
    """
    Given indexes = [a, b, c, ...], returns 
    matrix[a][b][c][...].
    """
    obj = matrix
    for ind in indexes:
        obj = obj[ind]
    return obj

def make_tupledict(matrix, *names):
    """Converts a matrix (in list of lists form) to a dictionary with tuples
    as keys.
    
    Arguments:
        matrix {List[List[...]]} -- matrix as list of lists (row-major order).
        names {List[List[Any]]} -- row/column names, in the order they are 
        in the list format.
    
    Returns:
        Dict[Tuple[...], int|float] -- dictionary indexed by name tuples.
    """
    d = tupledict()
    ranges = [range(len(x)) for x in names]
    for r in product(*ranges):
        if len(names) == 1:
            key = names[0][r[0]]
        else:
            key = tuple(name[i] for name, i in zip(names, r))
        d[key] = get_elem(matrix, r)
    return d
