import numpy as np
import re

def part1(inputdata):
    sum = 0;
    pattern_two_digits = re.compile(r"\D*(\d).*(\d)\D*")
    pattern_one_digit = re.compile(r"\D*(\d)\D*")
    for input in inputdata:
        matches = re.search(pattern_two_digits, input)
        if matches:
            sum += 10 * int(matches.group(1)) + int(matches.group(2))
        else:
            matches = re.search(pattern_one_digit, input)
            if matches:
                sum += 11 * int(matches.group(1))
            else:
                raise ValueError("no pattern found")
    print(f"the sum of all the calibration values is {sum}")
    
def part2(inputdata):
    number_mapping = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    pattern_two_numbers = re.compile(r"\.*(one|two|three|four|five|six|seven|eight|nine|\d).*(one|two|three|four|five|six|seven|eight|nine|\d)\.*")
    pattern_one_digit = re.compile(r"\D*(\d)\D*")
    sum = 0
    for input in inputdata:
        matches = re.search(pattern_two_numbers, input)
        if matches:
            number_1 = int(matches.group(1)) if matches.group(1) not in number_mapping.keys() else number_mapping[matches.group(1)]
            number_2 = int(matches.group(2)) if matches.group(2) not in number_mapping.keys() else number_mapping[matches.group(2)]
            sum += 10 * number_1 + number_2
        else:
            matches = re.search(pattern_one_digit, input)
            if matches:
                matches = re.search(pattern_one_digit, input)
                sum += 11 * int(matches.group(1))
            else:
                raise ValueError("no pattern found")
    print(f"the sum of all the calibration values is {sum}")
        

if __name__ == '__main__':
    inputfile = open(r'C:\Users\Daniel\Github\advent-of-code-2023\day01\input.txt', 'r')
    inputdata = np.asarray([line.strip() for line in inputfile])
    part1(inputdata)
    part2(inputdata)