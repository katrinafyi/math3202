from functools import lru_cache

def rocket():
    from gurobipy import Model, GRB
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

def multiplication_cards():
    CARDS = frozenset(range(10))
    BOXES = range(4)

    @lru_cache(None)
    def V(boxes, cards, trace=False): 
        if all(b is not None for b in boxes):
            x = boxes
            return ((10*x[0]+x[1])*(10*x[2]+x[3]), None)
        p = 1/len(cards)
        s = 0
        if trace: moves = {}
        # print(cards)
        for c in cards:
            v, i = min(
                (V(boxes[:i]+(c,)+boxes[i+1:], cards-{c} )[0], i)
                for i, a in enumerate(boxes) if a is None
            )
            if trace:
                print(c, i, v)
            if trace: moves[c] = i
            s += p * v
        return (s, moves if trace else None)
    
    print(V((None, )*4, (CARDS), 1))
    #print(V(2, (None, None, 4, 2), frozenset(CARDS)))
    print(V.cache_info())


if __name__ == "__main__":
    multiplication_cards()