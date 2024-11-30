file = list(open(r'input\02.txt'))

horizontal = 0
depth = 0
aim = 0

for input in file:
    if 'forward' in input:
        horizontal += int(input[-2])
        depth += aim * int(input[-2])
    if 'up' in input:
        aim -= int(input[-2])
    if 'down' in input:
        aim += int(input[-2])

print(f'task 1: {horizontal*depth}')