from gurobipy import * 
import FactoryPlanningStub as data

def make_tupledict(matrix, rows, cols):
    """Converts a matrix (in list of lists form) to a dictionary with tuples
    as keys.
    
    Arguments:
        matrix {List[List[int | float]]} -- matrix as list of lists (row-major order).
        rows {List[Any]} -- list of row keys.
        cols {List[Any]} -- list of column keys.
    
    Returns:
        Dict[Tuple[Any, Any], int|float] -- dictionary indexed by (row_key, col_key)
        tuples.
    """
    d = tupledict()
    for r, row in enumerate(matrix):
        for c, item in enumerate(row):
            d[rows[r], cols[c]] = item
    return d
def tutorial_5():
    P = [f'P{i+1}' for i in range(7)]
    M = ['Grind', 'VDrill', 'HDrill', 'Bore', 'Plane']
    T = [1, 2, 3, 4, 5, 6]

    AvailableMachines = dict(zip(M, [4, 2, 3, 1, 1]))
    Profit = dict(zip(P, [10, 6, 8, 4, 11, 9, 3]))
    TimeRequired = make_tupledict([
        [0.5, 0.1, 0.2, 0.05, 0.00],
        [0.7, 0.2, 0.0, 0.03, 0.00],
        [0.0, 0.0, 0.8, 0.00, 0.01],
        [0.0, 0.3, 0.0, 0.07, 0.00],
        [0.3, 0.0, 0.0, 0.10, 0.05],
        [0.2, 0.6, 0.0, 0.00, 0.00],
        [0.5, 0.0, 0.6, 0.08, 0.05]
    ], P, M)

    Maintenance =  make_tupledict([
        [1, 0, 0, 0, 0],
        [0, 0, 2, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 1]
    ], T, M)

    MarketLimits = make_tupledict([
        [ 500, 600, 300, 200,   0, 500],
        [1000, 500, 600, 300, 100, 500],
        [ 300, 200,   0, 400, 500, 100],
        [ 300,   0,   0, 500, 100, 300],
        [ 800, 400, 500, 200,1000,1100],
        [ 200, 300, 400,   0, 300, 500],
        [ 100, 150, 100, 100,   0,  60]
    ], P, T)

    StorageLimit = 100 
    ProductDesired = 50
    HoursPerDay = 16
    DaysPerMonth = 24

    class ProfitGetter(dict):
        def get(self, x, default=None):
            return Profit[x[0]]

    model = Model('Factory Planning')
    X = model.addVars(P, T, name='X', vtype=GRB.INTEGER) # produced
    Y = model.addVars(P, T, name='Y', obj=ProfitGetter(), vtype=GRB.INTEGER) # sold 
    Z = model.addVars(P, T, name='Z', obj=-0.5, vtype=GRB.INTEGER) # stored
    A = model.addVars(M, T, name='A', vtype=GRB.INTEGER) # number of machines of type m maintained in month t

    model.addConstrs(A.sum(m, '*') == AvailableMachines[m] for m in M)


    for t in T:
        if t > 1:
            model.addConstrs(Z[p,t] == X[p,t] - Y[p,t] + Z[p,t-1] for p in P)
        else:
            model.addConstrs(Z[p,t] == X[p,t] - Y[p,t] for p in P)

        # machine hours available in this month
        MachineHours = {
            m: (AvailableMachines[m]-A[m,t])*HoursPerDay*DaysPerMonth
            for m in M
        }
        # machine hours constraint
        model.addConstrs(
            quicksum(X[p,t]*TimeRequired[p,m] for p in P) <= MachineHours[m] for m in M
        )

        # market limits
        model.addConstrs(Y[p,t] <= MarketLimits[p,t] for p in P)

        # storage limits
        model.addConstrs(Z[p,t] <= StorageLimit for p in P)

    last = T[-1]
    model.addConstrs(Z[p,last] >= ProductDesired for p in P)



    model.modelSense = GRB.MAXIMIZE
    model.optimize()

    for t in T:
        print()
        print(f'== MONTH {t} ==')
        print('Produced: ', end='')
        for p in P:
            v = X[p,t]
            print(f'{p} = {v.x},  ', end='')
        print()
        print('Sold:     ', end='')
        for p in P:
            v = Y[p,t]
            print(f'{p} = {v.x},  ', end='')
        print()
        print('Stored:   ', end='')
        for p in P:
            v = Z[p,t]
            print(f'{p} = {v.x},  ', end='')
        print()
        print('Maintenance: ', end='')
        for m in M:
            v = A[m,t]
            print(f'{v.varname} = {v.x},  ', end='')
        print()


    print(model.getObjective())


    

if __name__ == "__main__":
    tutorial_5()