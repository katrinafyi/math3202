from functools import lru_cache

try:
    from gurobipy import *
except ImportError: pass

def word_game():
    from words import N, NBlanks, words as _words, v
    import string

    @lru_cache(None)
    def letter_counts(word: str):
        c = {'_': len(word)}
        for l in string.ascii_lowercase:
            c[l] = word.count(l)
        return c
        


    Words = [x[0].lower() for x in _words]
    Scores = dict(zip(Words, v))
    Letters = string.ascii_lowercase + '_'
    NumTiles = dict(zip(string.ascii_lowercase, N))
    NumTiles['_'] = NBlanks
    
    m = Model('Word Game')

    # number of each letter used in each word
    X = m.addVars(Words, Letters, name='X', vtype=GRB.INTEGER)
    Y = m.addVars(Words, name='Y', vtype=GRB.BINARY, obj=Scores)
    m.setAttr(GRB.Attr.ModelSense, GRB.MAXIMIZE)

    m.addConstrs( 
        X[w,l] <= n
        for w in Words
        for l, n in letter_counts(w).items()
    )

    m.addConstrs(
        len(w)*Y[w] <= X.sum(w, '*')
        for w in Words
    )

    m.addConstrs(
        X.sum('*', l) <= n for l, n in NumTiles.items()
    )

    m.optimize()

    for l in Letters:
        print(l, X.sum('*', l).getValue())

    for w in Words:
        if not Y[w].x: continue 
        print(w, Scores[w], end=': ')
        seen = set()
        for l in w + '_':
            if l in seen: continue 
            seen.add(l)
            if not X[w,l].x: continue
            print(l, round(X[w,l].x), end=', ')
        print()


def shopkeeper():
    DEMAND = [10, 20, 30, 30, 20, 20]
    ACTIONS = [0, 10, 20, 30, 40, 50, 60]

    @lru_cache(None)
    def V(t, s):
        if t >= len(DEMAND):
            return (0, ())

        return min(
            (
                20*min(a, 1) + 2*a 
                + 0.1*min(s+a-DEMAND[t], 40) 
                + V(t+1, min(s+a-DEMAND[t], 40))[0]
            , (a,) + V(t+1, min(s+a-DEMAND[t], 40))[1])
            for a in ACTIONS
            if s+a >= DEMAND[t]
        )

    print(V(0, 0))

if __name__ == "__main__":
    word_game()