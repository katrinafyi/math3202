from functools import lru_cache

B = (
    (-6.4, 0.25),
    (0, 0.5),
    (6.4, 0.25)
)

D_Sing = lambda i, b: (12 + 0.002*i + b)
def Sing(t, i, m):
    p = 0.004
    s = 0 
    for b, p_b in B:
        s += (p * p_b*V(t+1, i - D_Sing(i, b), 1) # found mate
            + (1-p) * p_b*V(t+1, i - D_Sing(i, b), m)) # haven't found mate
    return s

D_Forage = lambda i, b: 8 + 0.007*i + b
def Forage(t, i, m):
    p = 0.6
    s = 0 
    for b, p_b in B:
        s += (p * p_b*V(t+1, i - D_Forage(i, b) + 32, m) # found food
            + (1-p) * p_b*V(t+1, i - D_Forage(i, b), m)) # didn't find food
    return s

def Rest(t, i, m):
    return V(t+1, i-3.6, m) # deduct food. keep everything else the same.

Actions = (
    ('rest', Rest),
    ('sing', Sing),
    ('forage', Forage)
)
@lru_cache(maxsize=2**25)
def V_memoized(t, i, m):
    if i <= 0:
        return (0, 'dead')
    if t >= 150:
        if m:
            return (2, 'mate') 
        return (0, 'survived')
    
    running_max = -1
    running_action = None
    for action, f in Actions:
        x = f(t, i, m)
        if x > running_max:
            running_max = x
            running_action = action
        if t >= 75:
            break # break after first action which is rest.
    if running_max == 0:
        return (0, 'certain death')
    return (running_max, running_action)

def V_tuple(t, i, m):
    p = i - int(i)

    v1 = 0 
    a1 = None
    if p > 0: # if p = 0, only consider (v2, a2)
        v1, a1 = V_memoized(t, int(i)+1, m)
    v2, a2 = V_memoized(t, int(i), m) # p < 1 always
    return (p*v1 + (1-p)*v2, (a1, a2))

def V(t, i, m):
    return V_tuple(t, i, m)[0]

def bird_song():
    print(V_tuple(0, 117, 0))
    print(V_tuple(0, 118, 0))
    print(V_memoized.cache_info())
    
    sing_thresholds = []
    for t in range(0, 75):
        for i in range(500):
            if V_tuple(t, i, 0)[1][1] == 'sing':
                break 
        sing_thresholds.append(i)
    print(sing_thresholds)

if __name__ == "__main__":
    bird_song()