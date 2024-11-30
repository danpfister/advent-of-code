file = list(open(r'input\01.txt'))

previous = None
previoussum = None
counter1 = 0
counter2 = 0


for current in file:
    if previous != None:
        if int(current) > previous:
            counter1 += 1
    previous = int(current)


for index in range(len(file)-2):
    currentsum = int(file[index]) + int(file[index+1]) + int(file[index+2])
    if previoussum != None:
        if currentsum > previoussum:
            counter2 += 1
    previoussum = currentsum

print(f'task 1: {counter1}')
print(f'task 2: {counter2}')