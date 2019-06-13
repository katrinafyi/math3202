from functools import lru_cache

try:
    from gurobipy import * 
except ImportError: pass

def gas_drills():
    from gas_drills import S, DrillCost, Group as GroupSites

    m = Model('Gas Drill Sites')


    Sites = S 
    Groups = list(range(len(GroupSites)))

    # whether a site is drilled
    X = m.addVars(Sites, name='X', vtype=GRB.BINARY, obj=DrillCost)
    # number of sites used from each group
    Y = m.addVars(Groups, name='Y', vtype=GRB.INTEGER, ub=2)
    # binary whether penalty is paid for particular group
    Z = m.addVars(Groups, name='Z', vtype=GRB.BINARY, obj=10000)

    m.setAttr(GRB.Attr.ModelSense, GRB.MINIMIZE)

    m.addConstr(X.sum() == 20)

    m.addConstrs(
        Y[g] == X.sum(GroupSites[g]) 
        for g in Groups
    )

    m.addConstrs(
        Z[g] >= Y[g]-1 for g in Groups
    )

    m.optimize()

    for i, x in enumerate(X.values()):
        if x.x:
            print(x.varname, x.x, DrillCost[i])
    
    for g in Groups:
        print(Y[g].varname, Y[g].x, Z[g].varname, Z[g].x)

    


def optimal_hiring():
    SEASONS = ['Summer', 'Autumn', 'Winter', 'Spring', 'Summer']
    REQUIRED = [155, 120, 140, 100, 155]

    @lru_cache(maxsize=None)
    def V(t, n):
        if t >= len(SEASONS):
            return (0, ())
        
        return min(
            (200*(s-n)**2 
                + 2000*(s-REQUIRED[t]) 
                + V(t+1, s)[0], 
            (s-n, ) + V(t+1, s)[1])
            for s in range(REQUIRED[t], 155+1)
        )
    
    print(V(0, 155))

if __name__ == "__main__":
    gas_drills()