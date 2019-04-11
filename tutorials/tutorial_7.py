from gurobipy import * 

from util import *


def coal_line_maint():
    N = [f'N{i}' for i in range(10)]
    E = [f'E{i}' for i in range(16)]
    T = [f'Week {i}' for i in range(10)]

    Mines = ['N0', 'N1', 'N2']
    Ships = ['N8', 'N9']

    Throughput = make_tupledict(
        [100, 50, 60, 100, 80, 80, 20, 40, 40, 40, 40, 50, 50, 50, 75, 75], E)
    N_ = lambda l: [f'N{x}' for x in l]
    From = make_tupledict(
        N_([0, 0, 0, 3, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7]), E)
    To = make_tupledict(
        N_([4, 3, 3, 4, 5, 5, 7, 6, 6, 6, 6, 7, 7, 7, 0, 0]), E)


    EdgesInto = {n: [e for e in E if To[e] == n] for n in N}
    EdgesFrom = {n: [e for e in E if From[e] == n] for n in N}

    m = Model('Coal Line')
    X = m.addVars(E, T, name='X')
    Y = m.addVars(E, T, name='Y', vtype=GRB.BINARY)

    m.addConstrs(X[e,t] <= Throughput[e]*(1-Y[e,t]) 
        for e in E for t in T)
    m.addConstrs(X.sum(EdgesInto[n], t) - X.sum(EdgesFrom[n], t) == 0
        for n in N for t in T)

    m.addConstrs(Y.sum(e, '*') >= 1 for e in E)
    m.addConstrs(Y.sum('*', t) <= 2 for t in T)

    m.setObjective(X.sum(EdgesInto['N0'], '*'), GRB.MAXIMIZE)

    m.optimize()

    print('Average throughput:', m.objVal / len(T))

    for t in T:
        print()
        print(t)
        print('Throughput:', X.sum(EdgesInto['N0'], t).getValue())
        print('Maintenance:', [e for e in E if Y[e,t].x > 0.5])
    

if __name__ == "__main__":
    coal_line_maint()