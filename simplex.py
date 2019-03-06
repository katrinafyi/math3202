import sympy as sp
from collections import namedtuple

Solution = namedtuple('Solution', 'variables objective')

def iterate(basic, non_basic, c, A, b):
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
            print('UNBOUNDED PROBLEM')
            raise ValueError()

        # r is the index of the leaving variable
        r = min(ratios)[1]
        print('  exiting r', r)

        # remove r from basis cariables.
        basic.remove(r)
        non_basic.append(r)

        # add j to basic variables.
        basic.append(j)
        non_basic.remove(j)

    assert False

def optimise(c: list, A: list, b: list, num_vars):
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

    def optimise(self):
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

        return optimise(c, A, b, self.num_vars)


if __name__ == "__main__":
    (Simplex()
        .add_vars(2)
        .add_constraint([2, 1], LE, 100)
        .add_constraint([1, 1], LE, 80)
        .add_constraint([1, 0], LE, 40)
        .add_constraint([1, 0], GE, 40)
        # .add_constraint([1, 2], EQ, 25)
        .set_objective([3, 2])
        .optimise()
    )

    # optimise(
    #     [3, 2, 0, 0, 0],
    #     np.array([[2, 1, 1, 0, 0], [1, 1, 0, 1, 0], [1, 0, 0, 0, 1]]),
    #     [100, 80, 40])