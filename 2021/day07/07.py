import numpy as np
import re
from scipy.special import comb

file = open(r'input\07.txt', 'r')
line = file.readline()
inputdata = np.asarray(re.split(r'\D', line)[:-1], dtype=np.int32)

############################## PART 1 ##############################

fuelarray = np.zeros((1000), dtype=np.int32)
indices = np.arange(1000)

for input in inputdata:
    fuelarray = np.where(fuelarray != input, fuelarray + abs(indices - input), 0)

print(f"total fuel cost of task 1 is {np.min(fuelarray)} at position {np.argwhere(fuelarray == np.min(fuelarray))[0][0]}")

############################## PART 2 ##############################

fuelarray = np.zeros((1000), dtype=np.int32)
indices = np.arange(1000)

for input in inputdata:
    fuelarray = np.where(fuelarray != input, fuelarray + comb(abs(indices - input)+1, 2), 0)

print(f"total fuel cost of task 2 is {int(np.min(fuelarray))} at position {np.argwhere(fuelarray == np.min(fuelarray))[0][0]}")