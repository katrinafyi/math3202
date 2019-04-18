from functools import lru_cache
import sys

from typing import *

@lru_cache(maxsize=2**15)
def fib(n):
    if n == 0 or n == 1 or n == 2:
        return 1 
    return fib(n-1) + fib(n-2)

passing = {
    0: [0.2, 0.25, 0.1],
    1: [0.3, 0.3, 0.3],
    2: [0.35, 0.33, 0.4],
    3: [0.38, 0.35, 0.45],
    4: [0.4, 0.38, 0.5]
}

@lru_cache(maxsize=2**10)
def _solve_study(hours: int, subject: int): 
    if hours == 0 or subject > 2:
        return (1, ())
    
    min_prob = float('inf')
    min_x = None
    for x in range(0, hours+1): # x = hours at this subject
        _p, _x = _solve_study(hours-x, subject+1)
        p = (1-passing[x][subject])*_p
        if p < min_prob:
            min_prob = p
            min_x = (x, ) + _x
    return (min_prob, min_x)

def studying():
    return _solve_study(4, 0)

def _vladimir(games: int, delta: int):
    if games >= 2:
        if delta > 0:
            return (1, 'win')
        elif delta < 0:
            return (0, 'lose')
        return (0.45, 'bold')

    bold = (0.45*_vladimir(games+1, delta+1)[0] + 0.55*_vladimir(games+1, delta-1)[0], 'bold')
    cons = (0.9*_vladimir(games+1, delta)[0] + 0.1*_vladimir(games+1, delta-1)[0], 'cons')
    return max(bold, cons)

values = [25, 12, 8]
sizes = [7, 4, 3]

@lru_cache()
def knapsack(item: int, space: int):
    if space == 0 or item > 2:
        return (0, ())

    max_value = 0
    max_items = ()
    for n in range(space): # number of item 'i' to put in knapsack
        if n*sizes[item] > space: break
        
        v, i = knapsack(item+1, space-n*sizes[item])
        val = n*values[item] + v

        if val > max_value:
            max_value = val
            max_items = (n, ) + i

    return (max_value, max_items)

    

if __name__ == '__main__':
    # print(knapsack(0, 20))
    print(knapsack.cache_info())
    print(_vladimir(0, 0))
    # print(studying())
    # print(_solve_study.cache_info())
    # print(fib(int(sys.argv[1])))