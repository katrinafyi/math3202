from functools import lru_cache

@lru_cache(maxsize=2**10)
def V(j):
    if j == 0:
        return (9, 'next available') 
    a = 'here if possible' if j < V(j-1)[0] else 'skip' 
    return (0.1*min(j, V(j-1)[0]) + 0.9*V(j-1)[0], a)

def parking():
    for j in range(20):
        print(j, V(j))

if __name__ == "__main__":
    parking()