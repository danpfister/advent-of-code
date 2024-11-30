import numpy as np
import re

mapping_1 = {'A': 'm', 'K': 'l', 'Q': 'k', 'J': 'j', 'T': 'i',
           '9': 'h', '8': 'g', '7': 'f', '6': 'e', '5': 'd', '4': 'c', '3': 'b', '2': 'a'}

mapping_2 = {'A': 'm', 'K': 'l', 'Q': 'k', 'T': 'j',
           '9': 'i', '8': 'h', '7': 'g', '6': 'f', '5': 'e', '4': 'd', '3': 'c', '2': 'b', 'J': 'a'}

def find_type(hand: str, part2=False):
    card_count = {}
    for card in hand:
        if card in card_count:
            card_count[card] += 1
        else:
            card_count[card] = 1
    if part2 and 'J' in card_count.keys() and len(card_count) > 1: # add the jokers to the card with the highest count
        nr_of_jokers = card_count['J']
        del card_count['J']
        card_count[max(card_count, key=card_count.get)] += nr_of_jokers
    match len(card_count):
        case 5: # high-card
            return 0
        case 4: # one pair
            return 1
        case 3: # two pair or three of a kind
            if 3 not in card_count.values(): return 2 # two pair
            return 3 # 3 of a kind
        case 2: # four of a kind or full house
            if 4 not in card_count.values(): return 4 # full house
            return 5 # 4 of a kind
        case 1: # five of a kind
            return 6
            
            

def part1(inputdata):
    hands = [line[:5] for line in inputdata]
    bids = [int(line[6:]) for line in inputdata]
    
    tuples = [[find_type(hand), ''.join([mapping_1[card] for card in hand]), hand, bid] for hand, bid in zip(hands, bids)]
    sorted_by_type = sorted(tuples, key=lambda x: (x[0], x[1]))
    
    print(f"PART 1: the total winnings are: {sum([(index+1) * tuple[3] for index, tuple in enumerate(sorted_by_type)])}")
    
def part2(inputdata):
    hands = [line[:5] for line in inputdata]
    bids = [int(line[6:]) for line in inputdata]
    
    tuples = [[find_type(hand, part2=True), ''.join([mapping_2[card] for card in hand]), hand, bid] for hand, bid in zip(hands, bids)]
    sorted_by_type = sorted(tuples, key=lambda x: (x[0], x[1]))
    
    print(f"PART 2: the total winnings are: {sum([(index+1) * tuple[3] for index, tuple in enumerate(sorted_by_type)])}")
    
    

if __name__ == '__main__':
    inputfile = open(r'C:\Users\Daniel\Github\advent-of-code-2023\day07\input.txt', 'r')
    inputdata = np.asarray([line.strip() for line in inputfile])
    part1(inputdata)
    part2(inputdata)