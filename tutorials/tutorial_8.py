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
def _solve_study(hours: int, subject_hours: FrozenSet[int]): 
    if hours == 0:
        failing = 1
        for i, h in enumerate(subject_hours):
            failing *= (1-passing[h][i])
        return (1-failing, subject_hours)
    
    max_prob = 0
    max_subject = None
    for i in range(3): # i = subject index
        s = subject_hours
        # study that subject for one hour
        p, new_s = _solve_study(hours-1, s[:i] + (s[i]+1, ) + s[i+1:])
        if p > max_prob:
            max_subject = new_s
            max_prob = p 
    return (max_prob, max_subject)

def studying():
    return _solve_study(4, (0, 0, 0))

if __name__ == '__main__':
    print(studying())
    print(_solve_study.cache_info())
    # print(fib(int(sys.argv[1])))