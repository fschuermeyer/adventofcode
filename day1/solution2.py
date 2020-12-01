with open('data/day1.txt') as file:
    data = [int(i) for i in file.readlines()] 

year = 2020

for t in [(i,j) for i in data for j in data]:
    count1 = year - t[0]
    count2 = count1 - t[1]
 
    if count2 in data:
        solution = t[0] * t[1] * count2
        break

print(solution)