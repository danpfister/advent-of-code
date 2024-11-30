import numpy as np

def find_distance(galaxy_1, galaxy_2, empty, part2=False):
    x1, y1, x2, y2 = galaxy_1[0], galaxy_1[1], galaxy_2[0], galaxy_2[1]
    
    if x1 == x2 and y1 == y2: return 0 # return distance = 0 if it's the same galaxy
    
    if not part2:
        # add +1 for each row/column in between the two galaxies which is in the list of empty rows/columns
        difference_x = abs(x1 - x2) + sum([1 for x in range(min(x1, x2), max(x1, x2)+1) if x in empty[0]])
        difference_y = abs(y1 - y2) + sum([1 for y in range(min(y1, y2), max(y1, y2)+1) if y in empty[1]])
    else:
        # same as above but with 10^6 -1
        difference_x = abs(x1 - x2) + 999999*sum([1 for x in range(min(x1, x2), max(x1, x2)+1) if x in empty[0]])
        difference_y = abs(y1 - y2) + 999999*sum([1 for y in range(min(y1, y2), max(y1, y2)+1) if y in empty[1]])
        
    return difference_x + difference_y
    

def part1and2(inputdata):
    empty_x = [index for index in range(inputdata.shape[0]) if '#' not in inputdata[index, :]]
    empty_y = [index for index in range(inputdata.shape[1]) if '#' not in inputdata[:, index]]
    empty = [empty_x, empty_y]
    
    galaxies = np.argwhere(inputdata == '#')
    
    sum_lengths_1 = 0
    sum_lengths_2 = 0
    # go over each possible galaxy pair and divide by 2 (each pair is counted twice)
    # runs in O(n^2)
    for galaxy_1 in galaxies:
        for galaxy_2 in galaxies:
            sum_lengths_1 += find_distance(galaxy_1, galaxy_2, empty)
            sum_lengths_2 += find_distance(galaxy_1, galaxy_2, empty, part2=True)
            
    print(f"PART 1: the sum of the lengths between the galaxies is: {int(sum_lengths_1/2)}")
    print(f"PART 2: the sum of the lengths between the galaxies is: {int(sum_lengths_2/2)}")

if __name__ == '__main__':
    inputfile = open(r'C:\Users\Daniel\Github\advent-of-code-2023\day11\input.txt', 'r')
    inputdata = np.asarray([[char for char in line.strip()] for line in inputfile])
    part1and2(inputdata)