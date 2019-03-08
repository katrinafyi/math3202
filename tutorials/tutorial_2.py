from gurobipy import *

from typing import List, Sequence

def dot(u: Sequence[float], v: Sequence[float]):
    assert len(u) == len(v)
    return quicksum(u[i]*v[i] for i in range(len(u)))

def blending_problem():
    m = Model('Oil Blending')

    
    
    n = 5

    H = [8.8, 6.1, 2.0, 4.2, 5.0]
    h_min = 3
    h_max = 6

    all_oils = set(range(n))
    veg = set((0, 1))
    non_veg = all_oils - veg

    # decision variables - amount of each oil type
    X: List[Var] = [m.addVar() for _ in range(n)]
    

    # objective function coefficients
    c = [40, 30, 20, 40, 35]


    m.setObjective(dot(X, c), GRB.MAXIMIZE)

    m.addConstr(quicksum(X[i] for i in veg) <= 200)
    m.addConstr(quicksum(X[i] for i in non_veg) <= 250)
    m.addConstr(dot(X, H) - h_max*quicksum(X) <= 0)
    m.addConstr(dot(X, H) - h_min*quicksum(X) >= 0)
    
    m.optimize()

    print()
    for i, x in enumerate(X):
        print(i, x.x)


if __name__ == "__main__":
    blending_problem()