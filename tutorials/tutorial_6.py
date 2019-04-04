# from gurobipy import * 
import enum 
from collections import defaultdict, namedtuple

from itertools import product

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
    d = dict()
    ranges = [range(len(x)) for x in names]
    for r in product(*ranges):
        key = tuple(name[i] for name, i in zip(names, r))
        d[key] = get_elem(matrix, r)
    return d

class S(enum.Enum):
    EMPTY = enum.auto() 
    BLACK = enum.auto() 
    RED = enum.auto() 
    GREEN = enum.auto() 

grid_ = make_tupledict([
    '# # ',
    ' R #',
    '# # ',
    ' # G'
], range(4), range(4))
grid = defaultdict(lambda: None, grid_)



pieces = {
    0: {
        (-2, 0): ' ',
        (-1, 0): '#',
        (0, 0): ' ',
        (0, 1): '#',
    }
}

def rotate_cw(coordinates):
    return ((y, -x) for x, y in coordinates)

def rotations(piece):
    for i in range(4):
        x = piece.keys() 
        for _ in range(i):
            x = rotate_cw(x)
        yield dict(zip(x, piece.values()))

print(list(rotations(pieces[0])))

starting_positions = [(x, y) for x in range(4) for y in range(4)]

# We are using the mathematical coordinate system! 

def squares(grid=None):
    # squares = {}
    print(grid)
    used_squares = defaultdict(set)
    for p, piece in pieces.items():
        print('checking piece', piece)
        for x, y in starting_positions:
            print('checking starting position', x, y)
            for i, rotation in enumerate(rotations(piece)):
                rotation_squares = {(s[0]+x, s[1]+y): v for s, v in rotation.items()}
                # print('rot', rotation)
                valid = True
                for pos, value in rotation_squares.items():
                    # print('testing', pos)
                    if grid[pos] != value:
                        # print('mismatch', grid[pos], value)
                        valid = False
                        break
                if valid:
                    used_squares[p].add(tuple(rotation_squares.keys()))
                    print('  valid position of piece', p, 'with positions', rotation_squares)
    print(used_squares)

if __name__ == "__main__":
    squares(grid)

