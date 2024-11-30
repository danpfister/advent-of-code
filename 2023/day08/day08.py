import numpy as np
import re
import math

def parse_input(inputdata):
    instructions = inputdata[0]
    nodes = {}
    for line in inputdata[2:]:
        match = re.findall(r'([\dA-Z]{3})', line)
        nodes[match[0]] = [match[1], match[2]]
    return instructions, nodes

def part1(inputdata):
    instructions, nodes = parse_input(inputdata)
    current_node = 'AAA'
    steps_taken = 0
    
    while current_node != 'ZZZ': # repeat the whole block of instructions until 'ZZZ' is reached
        for instruction in instructions:
            if instruction == 'L':
                current_node = nodes[current_node][0]
            else:
                current_node = nodes[current_node][1]
            steps_taken += 1
    print(f"PART 1: the number of steps needed is: {steps_taken}")
    
def part2(inputdata):
    instructions, nodes = parse_input(inputdata)
    start_nodes = [node for node in nodes.keys() if node[-1] == 'A']
    end_nodes = [node for node in nodes.keys() if node[-1] == 'Z']
    steps_needed = {node: 0 for node in start_nodes}
    
    for node in start_nodes: # repeat below for all start nodes
        steps_taken = 0
        current_node = node
        while current_node not in end_nodes: # repeat the whole block of instructions until one of the end nodes is reached
            for instruction in instructions:
                if instruction == 'L':
                    current_node = nodes[current_node][0]
                else:
                    current_node = nodes[current_node][1]
                steps_taken += 1
        steps_needed[node] = steps_taken
    print(f"PART 2: the number of steps needed is: {math.lcm(*[steps for steps in steps_needed.values()])}")
            
            

if __name__ == '__main__':
    inputfile = open(r'C:\Users\Daniel\Github\advent-of-code-2023\day08\input.txt', 'r')
    inputdata = np.asarray([line.strip() for line in inputfile])
    part1(inputdata)
    part2(inputdata)