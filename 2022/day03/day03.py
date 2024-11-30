import numpy as np
import re

data = open(r"input.txt", 'r')
lines = [line.strip() for line in data]
inputdata = np.asarray(lines)

############################## PART 1 ##############################

priority_sum_1 = 0
for line in inputdata:
    compartment_1 = np.asarray([c for c in line[:len(line)//2]])
    compartment_2 = np.asarray([c for c in line[len(line)//2:]])

    item = np.intersect1d(compartment_1, compartment_2)[0]
    priority_sum_1 += ord(item)-96 if item.islower() else ord(item)-38
    
print(f"the sum of the priorities is {priority_sum_1}")

############################## PART 2 ##############################

priority_sum_2 = 0
for index in range(0, len(inputdata), 3):
    item = np.intersect1d(np.intersect1d(np.asarray([c for c in inputdata[index]]), np.asarray([c for c in inputdata[index+1]])), np.asarray([c for c in inputdata[index+2]]))[0] # lol
    priority_sum_2 += ord(item)-96 if item.islower() else ord(item)-38

print(f"the sum of the priorities is {priority_sum_2}")