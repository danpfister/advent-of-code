import numpy as np
import re

def part1and2(inputdata):
    points_total = 0
    matches_per_game = list()
    
    for card in inputdata:
        regex_matches = re.search(r'Card\s+\d+:\s(.*)\s\|\s(.*)', card)
        winning_numbers = regex_matches[1].split()
        own_numbers = regex_matches[2].split()
        
        matches = sum([1 if number in winning_numbers else 0 for number in own_numbers]) # count number of matches
        points_total += 2**(matches-1) if matches > 0 else 0 # points = 2^(matches-1) except if matches == 0
        matches_per_game.append(matches)
    print(f"the number of total points won is: {points_total}")
    
    matches_per_game = np.asarray(matches_per_game)    
    copies_per_game = np.ones_like(matches_per_game)
    
    for game in range(len(matches_per_game)):
        if matches_per_game[game] == 0:
            continue
        matches = matches_per_game[game]
        copies = copies_per_game[game]
        
        copies_per_game[game+1:game+matches+1] += copies
    print(f"the number of total scratchcards is: {sum(copies_per_game)}")
    

if __name__ == '__main__':
    inputfile = open(r'C:\Users\Daniel\Github\advent-of-code-2023\day04\input.txt', 'r')
    inputdata = np.asarray([line.strip() for line in inputfile])
    part1and2(inputdata)