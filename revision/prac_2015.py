from functools import lru_cache

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
    optimal_hiring()