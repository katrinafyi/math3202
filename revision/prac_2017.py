from gurobipy import *

def rocket():
    # Set up data
    Mass = [70, 90, 100, 110, 120, 130, 150, 180, 210, 220, 250, 280, 340, 350, 400]
    P = range(len(Mass))

    # A, B, C, D
    Sections = ["A", "B", "C", "D"]
    S = range(len(Sections))

    m = Model('Rocket Payload')
    X = m.addVars(P, S, vtype=GRB.BINARY, name='X')
    Y = m.addVars(P, S, name='Y', obj=1)

    m.addConstrs(Y[p,s] == X[p,s]*Mass[p] for p, s in X.keys())

    m.addConstrs(Y.sum('*', s) <= 1000 for s in S)
    m.addConstrs(X.sum('*', s) >= 3 for s in S)

    m.addConstr(Y.sum('*', 0) == Y.sum('*', 3))
    m.addConstr(Y.sum('*', 1) == Y.sum('*', 2))
    
    m.setAttr(GRB.Attr.ModelSense, GRB.MAXIMIZE)
    m.optimize()

if __name__ == "__main__":
    rocket()