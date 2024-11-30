import numpy as np

def parse_input(inputdata):
    data =  [line.split() for line in inputdata]
    return [[int(value) for value in history] for history in data]

def find_differences(values):
    return [values[i]-values[i-1] for i in range(1, len(values))]

def part1and2(inputdata):
    data = parse_input(inputdata)
    last_values_sum = 0
    first_values_sum = 0
    for history in data:
        current_sequence = history
        last_values, first_values = [], []
        while not all(value == 0 for value in current_sequence): # loop until all the differences are zero
            last_values.append(current_sequence[-1]) # only keep the last value
            first_values.append(current_sequence[0])
            differences = find_differences(current_sequence)
            current_sequence = differences
        # PART 1: the extrapolated value is the sum of the last values
        last_values_sum += sum(last_values)
        # PART 2: the extrapolated value is the sum with alternating sign of the first values
        first_values_sum += sum([first_values[i] if i%2==0 else -first_values[i] for i in range(len(first_values))])
    print(f"PART 1: the total sum of the extrapolated values is: {last_values_sum}")
    print(f"PART 2: the total sum of the extrapolated values is: {first_values_sum}")

if __name__ == '__main__':
    inputfile = open(r'C:\Users\Daniel\Github\advent-of-code-2023\day09\input.txt', 'r')
    inputdata = np.asarray([line.strip() for line in inputfile])
    part1and2(inputdata)