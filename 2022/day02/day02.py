import numpy as np
import re

data = open(r"input\input.txt", 'r')
lines = [line.strip() for line in data]
inputdata = np.asarray(lines)

'''
A: rock, B: paper, C: scissors - A: 65, B: 66, C: 67, X: 88, Y: 89, Z: 90
A (2) beats C (1),
B (0) beats A (2),
C (1) beats B (0)

ascii modulo 3: 2 0 1
ascii-1 modulo 3 1 2 0
'''

mapping = {2: 'A', 0: 'B', 1: 'C'}

############################## PART 1 ##############################
pick_points = {'A': 1, 'B': 2, 'C': 3}

score_1 = 0
for line in inputdata:
    match = re.match(re.compile(r'(\w)\s(\w)'), line)
    opponent_pick = ord(match.group(1))
    our_pick = ord(match.group(2)) - 23

    score_1 += pick_points[chr(our_pick)]

    if our_pick == opponent_pick: # draw
        score_1 += 3
    elif opponent_pick%3 == (our_pick-1)%3: # win and else loss
        score_1 += 6
print(f"your final score is {score_1}")

############################## PART 2 ##############################
outcome_points = {'X': 0, 'Y': 3, 'Z': 6}

score_2 = 0
for line in inputdata:
    match = re.match(re.compile(r'(\w)\s(\w)'), line)
    opponent_pick = ord(match.group(1))
    outcome = match.group(2)

    score_2 += outcome_points[outcome]

    if outcome == 'Y':
        score_2 += pick_points[chr(opponent_pick)]
    elif outcome == 'X':
        score_2 += pick_points[mapping[(opponent_pick-1)%3]]
    else:
        score_2 += pick_points[mapping[(opponent_pick-2)%3]]
print(f"your final score is {score_2}")