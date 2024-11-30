import numpy as np
import re

file = open(r'input\08.txt', 'r')
lines = [line.strip() for line in file.readlines()]
data_raw = np.asarray(lines)

inputdata = np.empty((200, 14), dtype=object)
for lineindex, line in enumerate(data_raw):
    split = re.split(r'\W+', line)
    for index, signal in enumerate(split):
        inputdata[lineindex][index] = signal

############################## PART 1 ##############################

numberOfDigits = np.zeros((10), dtype=np.int32)

for entry in inputdata:
    for index in range(10, 14):
        match len(entry[index]):
            case 2:
                numberOfDigits[1] += 1
            case 4:
                numberOfDigits[4] += 1
            case 3:
                numberOfDigits[7] += 1
            case 7:
                numberOfDigits[8] += 1
            case _:
                pass

print(f"Number of occurences of digits 1, 4, 7, 8: {np.sum(numberOfDigits)}")

############################## PART 2 ##############################

def compare(string1, string2):
    unique = []
    for char in string1:
        unique.append(char)
    for char in string2:
        if char in unique:
            unique.remove(char)
        else:
            unique.append(char)
    return unique

letters = 'abcdefg'
totalsum = 0

for entry in inputdata:
    configuration = {}
    lettercount = {}
    # count occurence of each signal
    for letter in letters:
        count = 0
        for index in range(10):
            if letter in entry[index]:
                count += 1
        lettercount[letter] = count
    # signal with 4 occurences is segment 4,
    # signal with 6 occurences is segment 1,
    # and signal with 9 occurences is segment 5
    for signal, count in lettercount.items():
        match count:
            case 4:
                configuration[4] = signal
            case 6:
                configuration[1] = signal
            case 9:
                configuration[5] = signal
            case _:
                pass
    # find 1 (to determine difference between 0 and 6 afterwards)
    one = None
    for index in range(10):
        match len(entry[index]):
            case 2:
                one = entry[index]
        if one:
            break
    # look at output signals and determine the digit
    values = ""
    for value in entry[10:14]:
        match len(value):
            case 2:
                values += '1'
            case 4:
                values += '4'
            case 3:
                values += '7'
            case 7:
                values += '8'
            case 5:
                # it's either a 2, 3 or 5
                if configuration[4] in value and configuration[1] not in value and configuration[5] not in value:
                    values += '2'
                elif configuration[4] not in value and configuration[1] not in value and configuration[5] in value:
                    values += '3'
                elif configuration[4] not in value and configuration[1] in value and configuration[5] in value:
                    values += '5'
                else:
                    print("something wrong")
            case 6:
                # it's either a 6, 9 or 0
                if configuration[4] in value and configuration[1] in value and configuration[5] in value:
                    # 6 or 0
                    if one[0] in value and one[1] in value:
                        values += '0'
                    else:
                        values += '6'
                elif configuration[4] not in value and configuration[1] in value and configuration[5] in value:
                    values += '9'
                else:
                    print("something wrong")
    print(values)
    totalsum += int(values)
print(totalsum)