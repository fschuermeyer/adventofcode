from functools import reduce
from operator import is_not
from functools import partial

# Solution with one Function

with open('data/day1.txt') as file:
    data = [int(i) for i in file.readlines()] 

def checkforSum(t,year):
    if reduce(lambda x,y: x+y,t) == year:
        return reduce(lambda x,y: x*y,t)

# Erster Part
print(list(filter(partial(is_not, None), [checkforSum([i,j],2020) for i in data for j in data]))[0])

# Zweiter Part
print(list(filter(partial(is_not, None), [checkforSum([i,j,z],2020) for i in data for j in data for z in data]))[0])

