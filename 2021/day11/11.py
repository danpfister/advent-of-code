import numpy as np
from scipy.signal import convolve

data = open(r"input\11.txt", 'r')
lines = [line.strip() for line in data]
raw = np.asarray(lines)

############################## PART 1 ##############################

test = np.asarray(['5483143223', '2745854711', '5264556173', '6141336146', '6357385478', '4167524645', '2176841721', '6882881134', '4846848554', '5283751526'])

energy = np.empty((raw.shape[0], raw.shape[0]))

for lineindex, line in enumerate(raw):
    for charindex, char in enumerate(line):
        energy[lineindex][charindex] = char

total_flashes = 0
for step in range(1000):
    flashed = np.zeros_like(energy, dtype=bool)
    energy += 1
    flashing = np.logical_and(energy > 9, np.logical_not(flashed))
    while np.any(flashing):
        flashed = np.bitwise_or(flashed, flashing)
        energy += convolve(flashing, np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]]), mode='same')
        flashing = np.logical_and(energy > 9, np.logical_not(flashed))
    energy[flashed] = 0
    total_flashes += np.sum(flashed)
    if step == 99:
        print(f"total flashes after 100 steps: {total_flashes}")
    if np.all(energy == 0):
        print(f"all octopuses flashing after {step + 1} steps")
        break