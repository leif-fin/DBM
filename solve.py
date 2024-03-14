from pulp import *

#1 initialize the model

model = LpProblem(name='problem5', sense=LpMaximize)

#define either Binary , Integer
#2 define the decision/feature variables
#A produce at least 10 units
#B produce at least 15 units
#C produce at least 5 units
A = LpVariable('A',lowBound=10,cat="Integer")
B = LpVariable('B',lowBound=15,cat="Integer")
C = LpVariable('C',lowBound=5,cat="Integer")

#3 objective function
#           A    B   C
#profit     20   30   40
model += 20*A + 30*B + 35*C

#requirement
#staff, Machining, Assembly resouces
#50 staffs working for 30 days, 1000 Maching hours for 30 days, 700 Assembly hours for 30 days
#     staff    Machining     Assembly
#A      0         5              3
#B      2        10              6
#C      3        20             10

model += 2*B + 3*C    <=50*30, "Staff constraint"
model += 5*A + 10*B + 20*C  <=1000 , "Maching constraint"
model += 3*A + 6*B + 10*C   <=700 , "Assembly constraint"

#5 solve the model
model.solve()

#6print out the result
print(A.varValue)
print(B.varValue)
print(C.varValue)
profit = pulp.value(model.objective)
print(profit)