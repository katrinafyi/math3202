import sympy as sp
from collections import namedtuple

from typing import List

Solution = namedtuple('Solution', 'variables objective')

def iterate(basic: List[int], non_basic: List[int],
            c: sp.Matrix, A: sp.Matrix, b: sp.Matrix) -> Solution:
    while True:
        print()
        print('ITERATING')

        print('basis', basic)

        # matrix of columns of A in the basis
        print()
        B = A[:, list(basic)]
        B_inv = B**-1
        print('B matrix:')
        sp.pprint(B)

        # basic feasible solution
        x_B = B_inv * b
        print('x_B', x_B)

        # cost coefficients of variables in the basis
        c_B = sp.Matrix([c[b] for b in basic])
        print('c_B', c_B)

        # objective function value
        z_B = c_B.dot(x_B)
        print('z_B', z_B)

        # compute dual variables
        y = (B_inv).T * c_B
        print('y', y)

        # iterate over non-basic variables to select one to enter
        feasible_entering_vars = []
        for j in non_basic:
            # compute reduced cost
            c_j_prime = c[j] - y.dot(A[:,j])

            if c_j_prime > 0:
                feasible_entering_vars.append((c_j_prime, j))

        if not feasible_entering_vars:
            # no further optimisation possible
            return Solution(x_B, z_B)

        print('c_j\', j_*', feasible_entering_vars)
        # entering variable with index j
        j = max(feasible_entering_vars)[1]
        print('  entering j', j)
        p_j = A[:,j]

        # determine leaving variable by element-wise dividing x_B and alpha_j.
        alpha_j = B_inv * p_j
        ratios = [(x_B[k] / alpha_j[k], basic[k]) for k in range(len(x_B)) if alpha_j[k] > 0]
        print('ratio test', ratios)

        if not ratios:
            raise ValueError('UNBOUNDED PROBLEM')

        # r is the index of the leaving variable
        r = min(ratios)[1]
        print('  exiting r', r)

        # remove r from basis variables.
        basic.remove(r)
        non_basic.append(r)

        # add j to basic variables.
        basic.append(j)
        non_basic.remove(j)

    assert False

def do_optimise(c: sp.Matrix, A: sp.Matrix, b: sp.Matrix, num_vars: int):
    # number of decision variables
    n = num_vars

    c = sp.Matrix(c)
    A = sp.Matrix(A)
    b = sp.Matrix(b)
    augmented = A.col_insert(A.shape[1], b)
    augmented.rref()

    # starting basic variables as slack/surplus variables
    basic = list(range(n, A.shape[1]))
    non_basic = list(range(n))
    print(list(basic), list(non_basic))

    print(iterate(basic, non_basic, c, A, b))

EQ = object()
LE = object()
GE = object()


class Simplex:
    def __init__(self):
        self.num_vars = 0
        self.constraints = []
        self.obj_coeff = []

    def add_var(self):
        self.num_vars += 1
        return self

    def add_vars(self, num_vars=1):
        self.num_vars += num_vars
        return self

    def add_constraint(self, coefficients, direction, constant):
        self.constraints.append((coefficients, direction, constant))
        return self

    def set_objective(self, coefficients):
        self.obj_coeff = coefficients
        return self

    def maximise(self):
        assert self.num_vars > 0

        # number of columns in A = num decision variables + num slack variables
        num_cols = (self.num_vars
            + sum(1 for constr in self.constraints if constr[1] is not EQ))

        extra_zeros = [0] * (num_cols - self.num_vars)

        b = []
        A = []
        c = self.obj_coeff + extra_zeros
        for i, constr in enumerate(self.constraints):
            row = constr[0]
            row.extend(extra_zeros)

            if constr[1] is not EQ:
                row[self.num_vars + i] = 1 if constr[1] is LE else -1

            A.append(row)
            b.append(constr[2])

        return do_optimise(c, A, b, self.num_vars)

def rsa_example():
    (Simplex()
        .add_vars(2)
        .add_constraint([2, 1], LE, 100)
        .add_constraint([1, 1], LE, 80)
        .add_constraint([1, 0], LE, 40)
        .add_constraint([1, 0], GE, 40)
        # .add_constraint([1, 2], EQ, 25)
        .set_objective([3, 2])
        .maximise()
    )

def farmer_jones():
    (Simplex()
        .add_vars(2)
        .add_constraint([20, 50], LE, 480) # time
        .add_constraint([4, 1], LE, 30) # eggs
        .add_constraint([0.25, 0.2], LE, 5) # milk
        .set_objective([4, 2])
        .maximise()
    )

def tutorial_2():
    # blending problem
    s = Simplex()
    s.add_vars(5)
    s.add_constraint([1, 1, 0, 0, 0], LE, 200)
    s.add_constraint([0, 0, 1, 1, 1], LE, 250)
    s.add_constraint([2.8, 0.1, -4, -1.8, -1], LE, 0)
    s.add_constraint([5.8, 3.1, -1, 1.2, 2], GE, 0)
    s.set_objective([40, 30, 20, 40, 35])
    s.maximise()

if __name__ == "__main__":
    tutorial_2()