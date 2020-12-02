with open('_data/day1.txt') as file:
    data = [int(i) for i in file.readlines()] 

year = 2020

for i in data:
    i = int(i)
    if (year - i) in data:
        solution = (year - i) * i
        break

print(solution)