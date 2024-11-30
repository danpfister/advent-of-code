import numpy as np
import re

file = open(r'input\06.txt', 'r')
line = file.readline()
inputdata = np.asarray(re.split(r'\D', line)[:-1], dtype=np.int32)


############################## PART 1 ##############################

currentfish = inputdata
for day in range(80):
    newfish = []
    for fish in currentfish:
        if fish > 0:
            newfish.append(fish - 1)
        else:
            newfish.append(6)
            newfish.append(8)
    currentfish = newfish

print(len(currentfish))

############################## PART 2 ##############################

# it's big brain time

currentfish = np.empty((9), dtype=np.int64)
for count in range(9):
    currentfish[count] = np.count_nonzero(inputdata == count)

for day in range(256):
    newfish = np.empty((9), dtype=np.int64)
    newfish[0] = currentfish[1]
    newfish[1] = currentfish[2]
    newfish[2] = currentfish[3]
    newfish[3] = currentfish[4]
    newfish[4] = currentfish[5]
    newfish[5] = currentfish[6]
    newfish[6] = currentfish[7] + currentfish[0]
    newfish[7] = currentfish[8]
    newfish[8] = currentfish[0]
    currentfish = newfish
print(np.sum(currentfish))