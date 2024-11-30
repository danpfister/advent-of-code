import numpy as np
import re
from scipy.spatial.distance import cityblock

def parse_input(inputdata):
    positions = np.empty((len(inputdata), 4), dtype=np.int64)
    for index, line in enumerate(inputdata):
        match = re.match(re.compile(r'Sensor at x=(-*\d+), y=(-*\d+): closest beacon is at x=(-*\d+), y=(-*\d+)'), line)
        positions[index, 0] = int(match.group(1))
        positions[index, 1] = int(match.group(2))
        positions[index, 2] = int(match.group(3))
        positions[index, 3] = int(match.group(4))
    return positions

def count_invalid_positions(positions, y_position):
    invalid_positions = set()
    for position in positions:
        sensor_x, sensor_y, beacon_x, beacon_y = position
        distance = cityblock([sensor_x, sensor_y], [beacon_x, beacon_y])
        y_offset = abs(sensor_y - y_position)
        if y_offset <= distance: # only then does the range reach the desired y position
            invalid_positions.update([pos for pos in range(sensor_x - (distance - y_offset), sensor_x + (distance - y_offset)+1)])
        if beacon_y == y_position: # remove beacon from invalid positions
            invalid_positions.discard(beacon_x)
    return len(invalid_positions)

if __name__ == "__main__":
    inputfile = open(r"input.txt", 'r')
    inputdata = np.asarray([line.strip() for line in inputfile])
    positions = parse_input(inputdata)
    print(f"the number of positions a beacon cannot be in at y position 2000000 is {count_invalid_positions(positions, 10)}")