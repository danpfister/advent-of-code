import numpy as np

def part1and2(inputdata):
    inputdata = np.pad(inputdata, 1, mode='constant', constant_values='.')
    symbols = ['#', '$', '%', '&', '*', '+', '-', '/', '=', '@']
    mask_symbols = np.isin(inputdata, symbols).astype(int)
    mask_gears = np.isin(inputdata, '*').astype(int)
    
    in_number = False
    start_index = 0
    sum_part_numbers = 0
    current_number = ""
    
    for i in range(1, inputdata.shape[0]-1): # iterate over rows
        for index, element in enumerate(inputdata[i]):
            if element.isdigit():
                if in_number: # currently in a number
                    current_number += element
                else: # entered a new number
                    in_number = True
                    current_number = element
                    start_index = index
            else: 
                if in_number: # exited a number
                    in_number = False
                    if np.any(mask_symbols[i-1:i+2, start_index-1:index+1] == 1): sum_part_numbers += int(current_number)
                    neighbors = mask_gears[i-1:i+2, start_index-1:index+1]
                    neighbors[neighbors != 0] += 1
                    mask_gears[i-1:i+2, start_index-1:index+1] = neighbors
                    current_number = ""
    print(f"the sum of all the part numbers is: {sum_part_numbers}")
    
    mask_gears = np.where(mask_gears == 3, 1, 0)
    
    # iterating twice over the whole array is bad but whatever, might optimize another time
    for i in range(1, inputdata.shape[0]-1): # iterate over rows
        for index, element in enumerate(inputdata[i]):
            if element.isdigit():
                if in_number: # currently in a number
                    current_number += element
                else: # entered a new number
                    in_number = True
                    current_number = element
                    start_index = index
            else: 
                if in_number: # exited a number
                    in_number = False
                    neighbors = mask_gears[i-1:i+2, start_index-1:index+1]
                    neighbors *= int(current_number)
    
    print(f"the sum of the gear ratios is: {np.sum(mask_gears)}")
    

if __name__ == '__main__':
    inputfile = open(r'C:\Users\Daniel\Github\advent-of-code-2023\day03\input.txt', 'r')
    inputdata = np.asarray([[c for c in line.strip()] for line in inputfile])
    part1and2(inputdata)