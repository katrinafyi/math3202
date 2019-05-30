from gurobipy import *
from itertools import product
from functools import lru_cache

Ports = ['Manly','Cleveland','Dunwich']
P = list(range(len(Ports)))
B = list(range(18))

Travel = [
	[29, 27, 21], [39, 18, 30], [40, 20, 31], [33, 19, 27], [35, 29, 36], [21, 23, 20],
	[30, 41, 32], [37, 27, 36], [20, 25, 34], [36, 28, 20], [24, 23, 25], [38, 22, 40], 
	[39, 19, 27], [30, 18, 28], [40, 20, 32], [21, 32, 40], [23, 18, 20], [31, 18, 20]
]

PortCapacity = [8, 8, 6]

def moreton_bay():
    m = Model('Moreton Bay Storm')

    # binary variables for whether boat b moves to port P
    X = m.addVars(B, P, name='X', obj=0, vtype=GRB.BINARY)
    MAX = m.addVar(name='MAX', vtype=GRB.CONTINUOUS, obj=1)
    
    m.addConstrs(X.sum('*', p) <= PortCapacity[p] for p in P)
    m.addConstrs(X.sum(b, '*') == 1 for b in B)

    m.addConstrs((MAX >= X[b,p]*Travel[b][p] for b, p in product(B, P)))
    m.setAttr(GRB.Attr.ModelSense, GRB.MINIMIZE)
    m.update()
    m.optimize()

    for b in B:
        port = [p for p in P if X[b,p].x]
        assert len(port) == 1
        port = port[0]
        print('Boat', b, 'goes to', port, 'in', Travel[b][port], 'time.')

def prisoners():
    Actions = ['coop', 'def']
    A = [0, 1] # 0 is cooperate, 1 is defect.
    Payoff = [
        [3, 0],
        [5, 1]
    ]

    prob_coop = lambda t, c: min(max(0.6 + 0.1*c - 0.2*(t-c), 0), 1)

    @lru_cache(maxsize=None)
    def V(t, c):
        if t >= 10:
            return (0, ('end', ))
        return max(
            (prob_coop(t, c)*Payoff[a][0]
            + (1-prob_coop(t, c))*Payoff[a][1]
            + V(t+1, c+1-a)[0], 
            (Actions[a], ) + V(t+1, c+1-a)[1])
            for a in A
        )
    
    print(V(0, 0))

if __name__ == "__main__":
    prisoners()
