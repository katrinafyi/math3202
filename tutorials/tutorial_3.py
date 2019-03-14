from gurobipy import * 

def blending_problem_2():
    model = Model('Blending Problem 2')

    Oils = range(5)
    Veg = [0, 1]
    NonVeg = [2, 3, 4]
    Time = range(6)

    Hardnesses = [8.8, 6.1, 2.0, 4.2, 5.0]

    Costs = [
        [-110, -130, -110, -120, -100, -90],
        [-120, -130, -140, -110, -120, -100],
        [-130, -110, -130, -120, -150, -140],
        [-110, -90, -100, -120, -110, -80],
        [-115, -115, -95, -125, -105, -135]
    ]

    Initial = [500]*len(Oils)

    HMin = 3
    HMax = 6

    VegMax = 200
    NonVegMax = 250

    StoreMax = 1000
    StoreCost = 5

    ProfitPerUnit = 150
    StorageCost = 5

    X = model.addVars(Oils, Time, obj=ProfitPerUnit, name='X')
    Y = model.addVars(Oils, Time, obj=Costs, name='Y')
    S = model.addVars(Oils, Time, obj=-StorageCost, name='S')

    # at each time step.
    for t in Time:
        # veg processing constraint
        model.addConstr(quicksum(X[v,t] for v in Veg) <= VegMax)
        # non-veg processing constraint
        model.addConstr(quicksum(X[nv,t] for nv in NonVeg) <= NonVegMax)

        # storage constraint
        model.addConstrs(S[i,t] <= StoreMax for i in Oils)

        # first month. use initial oil.
        if t == 0:
            model.addConstrs(S[i,t] == 500 - X[i,t] + Y[i,t] for i in Oils)
        else:
            # storage at end of this month is previous month's storage
            # minus processing plus purchases this month.
            model.addConstrs(S[i,t] == S[i,t-1] - X[i,t] + Y[i,t] for i in Oils)

    model.modelSense = GRB.MAXIMIZE
    model.optimize()
    
    format_list = lambda items: ' '.join(f'{k}: {v.x}' for k, v in items if v.x)

    for t in Time:
        print('Month', t)
        for d in (X, Y, S):
            for i in Oils:
                var = d[i,t]
                print(var.x, end=' ')
            print()

    pass 

if __name__ == "__main__":
    blending_problem_2()