import numpy as np
import re

def draw_cave(paths: list): # TODO could improve this by making cave size dynamic
    '''draw the paths into the cave matrix'''
    cave = np.full((250, 1000), '.') # first index is top to bottom, second index is left to right 
    for path in paths:
        previous_corner = None
        for corner in path:
            if previous_corner is None:
                cave[corner[0], corner[1]] = '#'
                previous_corner = corner
                continue
            if corner[0] == previous_corner[0]: # horizontal
                cave[corner[0], min(previous_corner[1], corner[1]):max(previous_corner[1], corner[1])+1] = '#'
            else: # vertical
                cave[min(previous_corner[0], corner[0]):max(previous_corner[0], corner[0])+1, corner[1]] = '#'
            previous_corner = corner
    
    return cave

def drop_sand(cave: np.ndarray, part: int) -> bool:
    '''drop a block of sand,
    returns:    for part 1: false if sand dropped into abyss, true else
                for part 2: false if sands final position is at the initial position, true else'''
    current_pos = np.array([0, 500])
    while True:
        if current_pos[0] == cave.shape[0]-1 and part == 1: # dropped into abyss
            return False
        if cave[current_pos[0]+1, current_pos[1]] == '.':
            current_pos += [1, 0]
            continue
        elif cave[current_pos[0]+1, current_pos[1]-1] == '.':
            current_pos += [1, -1]
            continue
        elif cave[current_pos[0]+1, current_pos[1]+1] == '.':
            current_pos += [1, 1]
            continue
        else:
            break
    cave[current_pos[0], current_pos[1]] = 'o'
    if part == 1: # return true if part 1
        return True
    if np.array_equal(current_pos, [0, 500]): # for part 2 return false if the sands final position is the initial position
        return False
    return True

def get_dimensions(paths: list):
    max_depth = 0
    for path in paths:
        for corner in path:
            max_depth = max(max_depth, corner[0])
    return max_depth
    
    
if __name__ == "__main__":
    inputfile = open(r"input.txt", 'r')
    inputdata = np.asarray([line.strip() for line in inputfile])
    paths = [[[int(corner[1]), int(corner[0])] for corner in re.findall(re.compile(r'(\d+),(\d+)(?: -> )*'), path)] for path in inputdata]

    cave = draw_cave(paths)
    nr_of_sandblocks = 0
    while drop_sand(cave, 1):
        nr_of_sandblocks += 1
        continue
    
    print(nr_of_sandblocks)
    
    paths.append([[get_dimensions(paths)+2, 0], [get_dimensions(paths)+2, 999]])
    cave = draw_cave(paths)
    nr_of_sandblocks = 0
    while True: # TODO fix this temp workaround the off-by-one bug (drop_sand() returns false one round "too early")
        nr_of_sandblocks += 1
        if not drop_sand(cave, 2):
            break
    
    print(nr_of_sandblocks)