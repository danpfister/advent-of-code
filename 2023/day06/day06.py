import numpy as np
import re
import time as t
import math

def parse_input_part_1(inputdata):
    time = [int(number) for number in re.findall(r'(\d+)', inputdata[0])]
    distance = [int(number) for number in re.findall(r'(\d+)', inputdata[1])]
    races = [[t, d] for t, d in zip(time, distance)]
    return races

def part1(inputdata):
    start_time = t.perf_counter()
    races = parse_input_part_1(inputdata)
    nr_of_ways_total = 1
    for time, distance in races:
        nr_of_ways = 0
        for hold_time in range(1, time):
            if hold_time * (time - hold_time) > distance: nr_of_ways += 1
        nr_of_ways_total *= nr_of_ways
    print(f"PART 1: the product of the number of ways is {nr_of_ways_total}. (Runtime={1e6*(t.perf_counter() - start_time):.2f}us)")
       
def part2(inputdata): # brute force -> Runtime: ~6s
    start_time = t.perf_counter()
    time = int(''.join([number for number in re.findall(r'(\d+)', inputdata[0])]))
    distance = int(''.join([number for number in re.findall(r'(\d+)', inputdata[1])]))
    
    nr_of_ways = 0
    for hold_time in range(1, time):
        if hold_time * (time - hold_time) > distance: nr_of_ways += 1
    print(f"PART 2: the product of the number of ways is {nr_of_ways}. (Runtime={(t.perf_counter() - start_time):.2f}s)")
    
def part2_opt(inputdata): # optimized -> Runtime: ~25us
    start_time = t.perf_counter()
    time = int(''.join([number for number in re.findall(r'(\d+)', inputdata[0])]))
    distance = int(''.join([number for number in re.findall(r'(\d+)', inputdata[1])]))
    
    root = math.sqrt(time**2 - 4*distance) # don't need to calculate root twice
    min_hold_time = math.ceil(time/2 - root/2 + 0.1) # find points where distance_over_record(hold_time) = 0
    max_hold_time = math.floor(time/2 + root/2 - 0.1) # +/- 0.1 to force rounding in edge cases where distance == record
    
    nr_of_ways = max_hold_time - min_hold_time + 1 # count all integers inbetween
    print(f"PART 2: the product of the number of ways is {nr_of_ways}. (Runtime={1e6*(t.perf_counter() - start_time):.2f}us)")

if __name__ == '__main__':
    inputfile = open(r'C:\Users\Daniel\Github\advent-of-code-2023\day06\input.txt', 'r')
    inputdata = np.asarray([line.strip() for line in inputfile])
    part1(inputdata)
    part2(inputdata)
    part2_opt(inputdata)