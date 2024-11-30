import numpy as np
import re


def map_source_to_destination_single(old_number, mappings):
    for mapping in mappings:
        destination, source, end = mapping
        if old_number in range(source, end): return destination - source + old_number # i.e. offset + previous value
    return old_number

def map_source_to_destination_block(block, mappings):
    block_start, block_end = block
    for mapping in mappings:
        mapping_destination, mapping_source, mapping_end = mapping
        offset = mapping_destination - mapping_source
        
        # block completely within one mapping -> return with offset
        if mapping_source <= block_start and mapping_end >= block_end:
            return [block_start + offset, block_end + offset], None
        
        # beginning of block within mapping -> return beginning with offset and put end onto unprocessed stack
        if mapping_source <= block_start and block_start < mapping_end and mapping_end < block_end:
            return [block_start + offset, mapping_end + offset], [mapping_end, block_end]
        
        # end of block within mapping -> return end with offset and put beginning onto unprocessed stack
        if mapping_source > block_start and block_end > mapping_source and mapping_end > block_end:
            return [mapping_source + offset, block_end + offset], [block_start, mapping_source]
        
        # block envelopes mapping -> return block with offset and beginning and end onto unprocessed stack
        if mapping_source > block_start and mapping_end < block_end:
            return [mapping_source + offset, mapping_end + offset], [[block_start, mapping_source], [mapping_end, block_end]]
        
    return [block_start, block_end], None # not in any mapping -> return without offset

def parse_mappings(inputdata):
    mappings = []
    for index in range(1, len(inputdata)):
        if inputdata[index] == '': continue
        if inputdata[index][0].isalpha():
            index += 1
            current_mapping = []
            while (index in range(1, len(inputdata)) and inputdata[index] != ''):
                numbers = [int(number) for number in re.findall(r'(\d+)', inputdata[index])]
                numbers = [numbers[0], numbers[1], numbers[1] + numbers[2]] # parse as (destination, source, end (non-inclusive))
                current_mapping.append(numbers)
                index += 1
            mappings.append(sorted(current_mapping, key=lambda x: x[1]))
    return mappings

def part1and2(inputdata):
    seeds = [int(seed) for seed in re.findall(r'\s(\d+)', inputdata[0])] # parse input
    mappings = parse_mappings(inputdata)
    lowest_location = np.inf
    
    for seed in seeds: # iterate over all seeds for part 1
        old_number = seed
        new_number = 0
        for mapping in mappings: # iterate over all maps
            new_number = map_source_to_destination_single(old_number, mapping)
            old_number = new_number
        if new_number < lowest_location: lowest_location = new_number
    print(f"PART 1: the initial seed with the lowest location has location: {lowest_location}")
    
    
    seeds = [[int(block[0]), int(block[1])] for block in re.findall(r'(\d+)\s(\d+)', inputdata[0])] # change how seeds are parsed for part 2
    seeds = [[seed[0], seed[0] + seed[1]] for seed in seeds]
    lowest_location = np.inf
    
    unprocessed_stack = seeds
    for mapping in mappings:
        next_stack = []
        while (len(unprocessed_stack) != 0): # loop until stack is empty, i.e. all blocks have gone through mapping
            processed_block, unprocessed_block = map_source_to_destination_block(unprocessed_stack.pop(0), mapping)
            next_stack.append(processed_block)
            if unprocessed_block is not None : # ugly but works
                if isinstance(unprocessed_block[0], list):
                    unprocessed_stack.extend(unprocessed_block)
                else:
                    unprocessed_stack.append(unprocessed_block)
        unprocessed_stack = next_stack
    print(f"PART 2: the initial seed with the lowest location has location: {min([item[0] for item in unprocessed_stack])}")
        
        
                
if __name__ == '__main__': # ~4ms for main
    inputfile = open(r'C:\Users\Daniel\Github\advent-of-code-2023\day05\input.txt', 'r')
    inputdata = np.asarray([line.strip() for line in inputfile])
    part1and2(inputdata)