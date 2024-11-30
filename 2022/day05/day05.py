import numpy as np
import re

data = open(r"input.txt", 'r')
lines = [line[:-1] for line in data]

stacks = np.full(9, '', dtype=object) # using object datatype kind of defeats the purpose of numpy, which is speed, but whatever
for line in lines[:8]:
    for stack, index in enumerate(range(1, 34, 4)): # hardcoded (for now)
        if (crate := line[index]) != '':
            stacks[stack] += crate

stacks_init = np.asarray([stack.strip() for stack in stacks], dtype=object) # 9 stacks, each stack read from top to bottom

############################## PART 1 ##############################

stacks = np.copy(stacks_init)
for line in lines[10:]:
    match = re.match(re.compile(r'move (\d+) from (\d+) to (\d+)'), line) # groups: 1: nr of items, 2: old stack, 3: new stack
    for movement in range(int(match.group(1))):
        stacks[int(match.group(3))-1] = stacks[int(match.group(2))-1][0] + stacks[int(match.group(3))-1] # add item to new stack
        stacks[int(match.group(2))-1] = stacks[int(match.group(2))-1][1:] # delete item from old stack

print(f"the first elements of the stacks are {''.join([stack[0] for stack in stacks])}")

############################## PART 1 ##############################

stacks = np.copy(stacks_init)
for line in lines[10:]:
    match = re.match(re.compile(r'move (\d+) from (\d+) to (\d+)'), line)
    stacks[int(match.group(3))-1] = stacks[int(match.group(2))-1][:int(match.group(1))] + stacks[int(match.group(3))-1]
    stacks[int(match.group(2))-1] = stacks[int(match.group(2))-1][int(match.group(1)):]

print(f"the first elements of the stacks are {''.join([stack[0] for stack in stacks])}")