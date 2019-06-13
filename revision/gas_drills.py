from gurobipy import *
import random

# 100 candidate sites
S = range(100)
random.seed(20)

# Drill cost at each site
DrillCost = [random.randint(15000,60000) for s in S]

# 30 groups with between 5 and 10 elements in every group
Group = [sorted(random.sample(S, random.randint(5,10))) for i in range(30)]
