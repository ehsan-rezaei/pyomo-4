# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 11:52:55 2019

@author: mcvet
"""

from pyomo.environ import * #every model starts with this to load the pyomo modeling environment
model= ConcreteModel() #Concrete models are immediately constructed
#model is a local variable to hold the model we are about to construct
model.x = Var(initialize=-1.2, bounds=(-2,2))
model.y= Var(initialize=1.0, bounds=(-2,2))
#model.give_name
#the name you assign the object to must be unique

model.obj = Objective(expr=(1-model.x)**2 + 100*(model.y-model.x**2)**2, sense=minimize)

model.limits = ConstraintList() #list of constraints
model.limits.add(30*model.a + 15*model.b + 10*model.c <=100)
model.limits.add(10*model.a + 25*model.b + 5*model.c <=75)
"""
Variables:
    model.a_variable = Var(within = NonNegativeReals)
    model.a_variable = Var(bounds=(0, None))
    
    within is optional and sets the variable domain
    there are several predefined domains e.g. Binary
    domain is assumed to be Reals if missing
Objective:
    model.obj = Objective(expr=, sense=)   
    if "sense" is omitted, Pyomo assumes minimization
    expr can be an expression, or any function-like object that returns an expression
    the objective expression is not a relational expression < >= etc
Constraints:
    model.c1=Constraint(expr=model.b + 5 * model.c <= model.a)
    constraints are relational expressions
    expr can also be a tuple
    model.limits = ConstraintList() creates a list where model.limits.add adds
    constraints to the list. the constraints don't have to be related.
"""
#constraints over indexes
model.IDX = range(10)
model.a=Var()
model.b=Var(model.IDX)    
model.c1=Constraint(expr=sum(model.b[i] for i in mode.IDX <=model.a))