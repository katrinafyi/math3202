from functools import lru_cache

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
    shopkeeper()