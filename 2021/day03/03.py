import numpy as np

file = list(open(r'input\03.txt', 'r'))

numberOfChars = len(file[0][:-1])

############################## PART 1 ##############################

gamma = '0b'

for position in range(numberOfChars):
    numberOfZeros = 0
    numberOfOnes = 0
    for line in file:
        if line[position] == '0':
            numberOfZeros += 1
        else:
            numberOfOnes += 1
    if numberOfZeros > numberOfOnes:
        gamma += '0'
    else:
        gamma += '1'

gamma_dec = int(gamma, 2)
epsilon_dec = ~int(gamma, 2) & 0xFFF

print(f"gamma * epsilon = {gamma_dec * epsilon_dec}")

############################## PART 2 ##############################

lines_oxy = np.asarray(file)
lines_co2 = np.asarray(file)

for position in range(numberOfChars):
    # find most common state of current position
    numberOfZeros = 0
    numberOfOnes = 0
    for line in lines_oxy:
        if line[position] == '0':
            numberOfZeros += 1
        else:
            numberOfOnes += 1
    commonState = '1' if (numberOfOnes >= numberOfZeros) else '0'
    # delete all entries where bit does not match most common state
    mask = np.ones(np.size(lines_oxy), dtype=bool)
    for index, line in enumerate(lines_oxy):
        if line[position] == commonState:
            mask[index] = False
    lines_oxy = np.delete(lines_oxy, mask)
    if len(lines_oxy) == 1:
        break

for position in range(numberOfChars):
    # same as above
    numberOfZeros = 0
    numberOfOnes = 0
    for line in lines_co2:
        if line[position] == '0':
            numberOfZeros += 1
        else:
            numberOfOnes += 1
    commonState = '1' if (numberOfOnes >= numberOfZeros) else '0'
    # same as above, just inverted
    mask = np.ones(np.size(lines_co2), dtype=bool)
    for index, line in enumerate(lines_co2):
        if line[position] != commonState:
            mask[index] = False
    lines_co2 = np.delete(lines_co2, mask)
    if len(lines_co2) == 1:
        break

oxygen = int(lines_oxy[0], 2)
co2 = int(lines_co2[0], 2)
print(f"oxygen * co2: {oxygen * co2}")