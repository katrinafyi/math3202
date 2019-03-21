from gurobipy import *

m = Model()
x1 = m.addVar()
x2 = m.addVar()

m.setObjective(3*x1+2*x2,GRB.MAXIMIZE)

c1 = m.addConstr(2*x1+x2<=100)
c2 = m.addConstr(x1+x2<=80)
c3 = m.addConstr(x1<=40)

m.optimize()

# RC of basic variables is 0
# For non-basic it is how much their price must change for them
# to be considered as basic
# SAObjLow and SAObjUp indicate the range of objective values before
# the basis will change
print('X1: Value', x1.x, 'RC', x1.rc, 'ObjLow', x1.SAObjLow, 'ObjUp', x1.SAObjUp)
print('X2: Value', x2.x, 'RC', x2.rc, 'ObjLow', x2.SAObjLow, 'ObjUp', x2.SAObjUp)

# At least one of slack or the dual is 0 for every constraint
# SARHSLow and SARHSUp indicate the range of over which the basis will
# stay the same
print('C1: Slack', c1.slack, 'Dual', c1.pi, 'RHSLow', c1.SARHSLow, 'RHSUp', c1.SARHSUp)
print('C2: Slack', c2.slack, 'Dual', c2.pi, 'RHSLow', c2.SARHSLow, 'RHSUp', c2.SARHSUp)
print('C1: Slack', c3.slack, 'Dual', c3.pi, 'RHSLow', c3.SARHSLow, 'RHSUp', c3.SARHSUp)