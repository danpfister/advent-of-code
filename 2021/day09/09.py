import numpy as np
import re
import cv2 as cv
from matplotlib import pyplot as plt
import random

data = open(r"input\09.txt", 'r')
lines = [line.strip() for line in data]
raw = np.asarray(lines)

inputdata = np.full((102, 102), 9)
for lineindex, line in enumerate(raw):
    for charindex, char in enumerate(line):
        inputdata[lineindex+1][charindex+1] = char

data_test = open(r"input\09_test.txt", 'r')
lines_test = [line.strip() for line in data_test]
raw_test = np.asarray(lines_test)

inputdata_test = np.full((7, 12), 9)
for lineindex, line in enumerate(raw_test):
    for charindex, char in enumerate(line):
        inputdata_test[lineindex+1][charindex+1] = char

# enable for testing
#inputdata = inputdata_test

############################## PART 1 ##############################

total = 0
lowpoints = np.zeros(inputdata.shape, dtype=bool)

for x in range(1, inputdata.shape[0]):
    for y in range(1, inputdata.shape[1]):
        if inputdata[x][y] < inputdata[x][y-1] and inputdata[x][y] < inputdata[x-1][y] and inputdata[x][y] < inputdata[x][y+1] and inputdata[x][y] < inputdata[x+1][y]:
            total += 1 + inputdata[x][y]
            lowpoints[x][y] = True

print(total)
print(np.sum(lowpoints))

############################## PART 2 ##############################

inputdata = np.array(inputdata*255/9, dtype=np.uint8)
_, inputdata_bin = cv.threshold(inputdata, 255*8.5/9, 255, cv.THRESH_BINARY_INV)

total_labels, label_ids = cv.connectedComponents(inputdata_bin, connectivity=4)

areas = []
for label in range(1, total_labels):
    size = len(np.argwhere(label_ids == label))
    areas.append(size)
    print(f"basin {label} has {size} tiles")

areas.sort(reverse=True)
print(f"endresult: {areas[0] * areas[1] * areas[2]}")

# colour the basins for fun
coloured = cv.merge((inputdata_bin, inputdata_bin, inputdata_bin))
for label in range(1, total_labels):
    coloured[label_ids == label] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

cv.imshow("blackwhite", coloured)
cv.imwrite(r"output\09.png", coloured)
cv.waitKey(0)