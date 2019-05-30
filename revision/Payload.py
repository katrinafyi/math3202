from gurobipy import *

# Set up data
Mass = [70, 90, 100, 110, 120, 130, 150, 180, 210, 220, 250, 280, 340, 350, 400]
M = range(len(Mass))

# A, B, C, D
Sections = ["A", "B", "C", "D"]
S = range(len(Sections))


pb = Model('Payload Balance')

# Dictionary comprehension
# Package m is in compartment s
X = {(m,s): pb.addVar(vtype=GRB.BINARY) for m in M for s in S}

# Balance constraints (A = D and B = C)
pb.addConstr(quicksum(Mass[m]*X[m,0] for m in M) == quicksum(Mass[m]*X[m,3] for m in M))
pb.addConstr(quicksum(Mass[m]*X[m,1] for m in M) == quicksum(Mass[m]*X[m,2] for m in M))

# Each package must be packed 
for m in M:
	pb.addConstr(quicksum(X[m,s] for s in S) == 1)

# Each section must contain at least three packages
# and have total weight no more than 1000 kg
for s in S:
	pb.addConstr(quicksum(X[m,s] for m in M) >= 3)
	pb.addConstr(quicksum(Mass[m]*X[m,s] for m in M) <= 1000)
	
pb.optimize()

for s in S:
	print (Sections[s])
	for m in M:
		if X[m,s].x > 0.90:
			print (m, Mass[m])