# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 09:57:35 2019

@author: Kenton
"""

from gurobipy import *

from .Diet import *

def farmer_jones():
    # model
    m = Model('Farmer Jones')

    # variables
    x_ch = m.addVar()
    x_pl = m.addVar()

    # objective
    m.setObjective(4*x_ch + 2*x_pl, GRB.MAXIMIZE)

    # constraints
    m.addConstr(20*x_ch + 50*x_pl <= 480) # time
    m.addConstr(4*x_ch + x_pl <= 30) # eggs
    m.addConstr(0.26*x_ch + 0.2*x_pl <= 5) # milk

    m.optimize()

    print(x_ch.x, x_pl.x)

def farmer_jones_2():
    C = ['chocolate', 'plain']
    I = ['time', 'eggs', 'milk']

    revenue = [4, 2]
    usage = [[20, 50],
             [4, 1],
             [0.25, 0.2]]
    available = [480, 30, 5]

    m = Model('Farmer Jones')

    X = [m.addVar() for _ in C]

    m.setObjective(quicksum(revenue[c]*X[c] for c in range(len(C))),
                            GRB.MAXIMIZE)

    for i in range(len(I)):
        m.addConstr(quicksum(usage[i][c]*X[c] for c in range(len(C))) <= available[i])

    m.optimize()

    for x in X:
        print(x.x)

def stigler():
    m = Model('Stigler Diet')

    X = [m.addVar() for f in F]

    for n in N:
        m.addConstr(DMIN[n] <= quicksum(NV[f][n]*X[f] for f in F))
        m.addConstr(quicksum(NV[f][n]*X[f] for f in F) <= DMAX[n])

    m.setObjective(quicksum(C[f]*X[f] for f in F), GRB.MINIMIZE)

    m.optimize()

    print('\n'.join([Food[i] + ': ' + str(x.x) for i, x in enumerate(X)]))

if __name__ == "__main__":
    farmer_jones()

