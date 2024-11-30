import numpy as np
import re

data = open(r"input.txt", 'r')
lines = [line.strip() for line in data]
inputdata = np.asarray(lines)

############################## PART 1 ##############################

contain_count = 0
for line in inputdata:
    match = re.match(re.compile(r'(\d+)-(\d+),(\d+)-(\d+)'), line) # groups: 1: start1, 2: end1, 3: start2, 4: end2
    start_1, end_1, start_2, end_2 = int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))

    if (start_1 <= start_2 and end_1 >= end_2) or (start_1 >= start_2 and end_1 <= end_2):
        contain_count += 1

print(f"the number of pairs contained within another is {contain_count}")

############################## PART 2 ##############################

overlap_count = 0
for line in inputdata:
    match = re.match(re.compile(r'(\d+)-(\d+),(\d+)-(\d+)'), line) # groups: 1: start1, 2: end1, 3: start2, 4: end2
    start_1, end_1, start_2, end_2 = int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))

    work_1, work_2 = np.arange(start_1, end_1+1), np.arange(start_2, end_2+1)
    if len(np.intersect1d(work_1, work_2)) != 0:
        overlap_count += 1

print(f"the number of pairs overlapping with eachother is {overlap_count}")