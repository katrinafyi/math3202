from functools import lru_cache

distances = [
    [0, 143, 108, 118, 121, 88, 121, 57, 92],    # home
    [143, 0, 35, 63, 108, 228, 182, 73, 162],    # A
    [108, 35, 0, 45, 86, 193, 165, 42, 129],     # B
    [118, 63, 45, 0, 46, 190, 203, 73, 105],     # C
    [121, 108, 86, 46, 0, 172, 224, 98, 71],     # D
    [88, 228, 193, 190, 172, 0, 174, 160, 108],  # E
    [121, 182, 165, 203, 224, 174, 0, 129, 212], # F
    [57, 73, 42, 73, 98, 160, 129, 0, 117],      # G
    [92, 162, 129, 105, 71, 108, 212, 117, 0]    # H
]

sales = [
    [0.0, 0.0, 0.0], # Home
    [0.3, 0.4, 0.3], # A
    [0.2, 0.5, 0.3], # B
    [0.2, 0.7, 0.1], # C
    [0.3, 0.5, 0.2], # D
    [0.3, 0.6, 0.1], # E
    [0.4, 0.3, 0.3], # F
    [0.0, 0.3, 0.7], # G 
    [0.1, 0.1, 0.8]  # H
]

Cities = range(len(sales))

expected = [500*(0*sales[k][0] + 1*sales[k][1] + 2*sales[k][2]) for k in Cities]

from typing import NamedTuple, FrozenSet
class Label(NamedTuple):
    node: int
    cost: int 
    paintings_left: int 
    cities_left: FrozenSet[int]
    parent: int

def travelling_artist():
    all_labels = {Label(0, 0, 1, frozenset(range(9), None))}
    pending_labels = set(all_labels)
    
    def add_label(label):
        all_labels.add(label)
        pending_labels.add(label)

    while True:
        l = min(pending_labels, key=lambda l: l.cost)
        pending_labels.remove(l)

        if len(l.cities_left) == 8 == 0:
            if l.node == 0:
                return l
            add_label(Label(
                0, l.cost + distances[l.node, 0], 
                0, l.cities_left, l.node))
            continue
        for city in range(8):
            city += 1 # ignore home


def travelling_artist_2():
    cities = frozenset(Cities)
    
    @lru_cache(maxsize=2**16)
    def solve(current: int, visited: FrozenSet[int]):
        if len(visited) == 4:
            return (-distances[current][0], (0, ))

        running_max = 0
        running_sol = None
        for city in cities-visited:
            x, sol = solve(city, visited | {city})
            x += expected[city] - distances[current][city]
            if x > running_max:
                running_max = x 
                running_sol = (city, ) + sol
        return (running_max, running_sol)

    print(solve(0, frozenset()))

cities = frozenset(Cities)
    
@lru_cache(maxsize=2**16)
def solve(current: int, paintings: int, visited: FrozenSet[int]):
    # print(current, paintings, visited)
    if paintings == 0:
        return (-distances[current][0], (0, ))

    running_max = 0
    running_sol = None
    for city in cities-visited:
        e_profit = -distances[current][city] # flat cost to go to this city
        for p in range(2): # num of paintings sold at this city
            if p > paintings: # cannot sell more than we have.
                continue
            # expected profit by going to this city
            e_profit += sales[city][p] * (500*p + solve(
                city, 
                paintings-p,
                visited | {city})[0])
        if e_profit > running_max:
            running_max = e_profit
            running_sol = city
    return (running_max, running_sol)
    
def travelling_artist_B():
    print(solve(0, 5, frozenset()))
    # print(solve.cache_info())

if __name__ == "__main__":
    travelling_artist_2()
    travelling_artist_B()