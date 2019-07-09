# -*- coding: utf-8 -*-
"""
Determine the set of P warehouses chosen from N candidates that minimizes the total
cost of serving all customers M where d (n,m) is the cost of serving customer m from
warehouse location n."""

from pyomo.environ import * #every model starts with this to load the pyomo modeling environment
N = 3
M = 4
P = 3
d = {(1, 1): 1.7, (1, 2): 7.2, (1, 3): 9.0, (1, 4): 8.3, (2, 1): 2.9, (2, 2): 6.3, (2, 3): 9.8, (2, 4): 0.7, (3, 1): 4.5, (3, 2): 4.8, (3, 3): 4.2, (3, 4): 9.3}
model= ConcreteModel()
model.Locations = range(N)
model.Customers = range(M)
model.x = Var(model.Locations, model.Customers, bounds=(0.0,1.0))
model.y = Var(model.Locations, within=Binary)

#model.obj=Objective(expr=sum(d[n,m]*model.x[n,m] for n in model.Locations for m in model.Customers))
model.obj = Objective( expr = sum( d[n,m]*model.x[n,m] for n in model.Locations for m in model.Customers ) )
model.single_x=ConstraintList()
model.single_x.add(sum(model.x[n,m] for n in model.Locations)==1.0)

model.bound_y = ConstraintList()
for n in model.Locations:
    for m in model.Customers:
        model.bound_y.add(model.x[n,m] < model.y[n])

model.num_facilities = Constraint(expr=sum(model.y[n] for n in model.Locations)==P)

#Passing to solver
pyomo solve <concrete p-median.py> [--solver=<glpk>] [--summary]