import numpy as np
import re

def parse_input(inputdata):
    cubes = np.empty((inputdata.shape[0], 3))
    for index, cube in enumerate(inputdata):
        match = re.match(re.compile(r'(\d+),(\d+),(\d+)'), cube)
        cubes[index, 0] = int(match.group(1))
        cubes[index, 1] = int(match.group(2))
        cubes[index, 2] = int(match.group(3))
    return cubes

def count_faces(cubes): # ultra slow but it works
    directions = np.asarray([[0, 0, -1], [0, 0, 1], [0, -1, 0], [0, 1, 0], [-1, 0, 0], [1, 0, 0]])
    free_faces = 0
    for cube in cubes:
        for direction in directions:
            free_faces += ~np.any([np.array_equal(cube+direction, c) for c in cubes])
    return free_faces
    
if __name__ == "__main__":
    inputfile = open(r"input.txt", 'r')
    inputdata = np.asarray([line.strip() for line in inputfile])
    cubes = parse_input(inputdata)
    print(f"the number of free faces is {count_faces(cubes)}")