from gurobipy import * 
import numpy as np 

def var_matrix(model: Model, rows, cols, prefix=''):
    variables = []
    for r in rows:
        variables.append([])
        for c in cols:
            variables[-1].append(model.addVar(name=f'{prefix}{r}{c}'))
    return np.array(variables)

def print_vars(text, variables):
    print(text, end=' ')
    for v in variables:
        print(round(v.x), end=' ')
    print()

def blending_problem_2():
    model = Model('Blending Problem 2')

    Oils = range(5)
    Veg = [0, 1]
    NonVeg = [2, 3, 4]
    Time = range(6)

    Hardnesses = np.array([8.8, 6.1, 2.0, 4.2, 5.0])

    Costs = np.array([
        [110, 130, 110, 120, 100, 90],
        [120, 130, 140, 110, 120, 100],
        [130, 110, 130, 120, 150, 140],
        [110, 90, 100, 120, 110, 80],
        [115, 115, 95, 125, 105, 135]
    ])

    Initial = np.array([500]*len(Oils))

    HMin = 3
    HMax = 6

    VegMax = 200
    NonVegMax = 250

    StoreMax = 1000
    StoreCost = 5

    X = var_matrix(model, Oils, Time, 'x_')
    Y = var_matrix(model, Oils, Time, 'y_')
    S = var_matrix(model, Oils, Time, 's_')

    # at each time step.
    for t in Time:
        # veg processing constraint
        model.addConstr(quicksum(X[Veg,t]) <= VegMax)
        # non-veg processing constraint
        model.addConstr(quicksum(X[NonVeg,t]) <= NonVegMax)

        for i in Oils:
            # storage constraint
            model.addConstr(S[i,t] <= StoreMax)

            # first month. use initial oil.
            if t == 0:
                model.addConstr(S[i,t] == 500 - X[i,t] + Y[i,t])
            else:
                # storage at end of this month is previous month's storage
                # minus processing plus purchases this month.
                model.addConstr(S[i,t] == S[i,t-1] - X[i,t] + Y[i,t])

    OilOnes = np.ones(len(Oils))
    TimeOnes = np.ones(len(Time))

    # parts of the objective 
    Income = quicksum(150*X[i,t] for i in Oils for t in Time)

    BuyingCost = quicksum(Y[i,t]*Costs[i,t] for i in Oils for t in Time)

    StorageCost = quicksum(5*S[i,t] for i in Oils for t in Time)

    model.setObjective(Income - StorageCost - BuyingCost, GRB.MAXIMIZE)
    model.optimize()

    for t in Time:
        print('Month', t)
        print_vars('X', X[:,t])
        print_vars('Y', Y[:,t])
        print_vars('S', S[:,t])

    pass 

if __name__ == "__main__":
    blending_problem_2()