import numpy as np
import cv2 as cv
from colour import Color

############################## PART 1&2 ##############################

def handle_forest(inputdata):
    visible = np.zeros_like(inputdata, dtype=bool)
    scenic_score = np.empty_like(inputdata)

    for row in range(inputdata.shape[0]):
        for tree in range(inputdata.shape[1]):
            current_tree = inputdata[row][tree]
            orientations = [inputdata[:row, tree][::-1], inputdata[row, :tree][::-1], inputdata[row+1:, tree], inputdata[row, tree+1:]] # counter clockwise starting from upwards
            view_distances = np.empty(4)
            for index, orientation in enumerate(orientations):
                current_view_distance = 0
                for next_tree in orientation:
                    current_view_distance += 1
                    if next_tree >= current_tree:
                        break
                view_distances[index] = current_view_distance
                if np.all(orientation < current_tree):
                    visible[row][tree] = True
            scenic_score[row][tree] = np.prod(view_distances)

    print(f"the number of visible trees is {np.sum(visible)}")
    print(f"the tree at position {np.argwhere(scenic_score == np.max(scenic_score))[0]} has the overall maximum scenic score {np.max(scenic_score)}")
    
    return visible, scenic_score

def draw_visible(visible):
    white = list(Color('#FFFFF0').get_rgb())
    green = list(Color('#006400').get_rgb())
    coloured = np.array([[green if tree else white for tree in row] for row in visible])
    coloured *= 255
    image = cv.resize(coloured, (coloured.shape[1]*4, coloured.shape[0]*4), interpolation=cv.INTER_AREA)
    cv.imwrite(r'.\visuals\08_visible_trees.png', image)

if __name__ == "__main__":
    data = open(r"input.txt", 'r')
    inputdata = np.asarray([[int(c) for c in line.strip()] for line in data])
    visible, scenic_score = handle_forest(inputdata)
    draw_visible(visible)