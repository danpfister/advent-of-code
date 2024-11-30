import numpy as np

data = open(r"input\10.txt", 'r')
lines = [line.strip() for line in data]
raw = np.asarray(lines)

############################## PART 1 ##############################

begin = ['(', '[', '{', '<']
end = [')', ']', '}', '>']
score = {')': 3, ']': 57, '}': 1197, '>': 25137} 
totalscore = 0
not_corrupt_mask = np.ones(raw.shape, dtype=bool)
stacks = np.empty(raw.shape, dtype=object)

for lineindex, line in enumerate(raw):
    stack = []
    for char in line:
        if char in begin:
            stack.append(char)
        elif char in end:
            if (popped := stack.pop()) != begin[end.index(char)]:
                #print(f"corrupted: expected {end[begin.index(popped)]} got {char}")
                totalscore += score[char]
                not_corrupt_mask[lineindex] = False
                break
        else:
            print("something is very wrong")
    temp = ''.join(stack)
    stacks[lineindex] = temp
print(f"total score is: {totalscore}")

############################## PART 2 ##############################

score_2 = {'(': 1, '[': 2, '{': 3, '<': 4}

not_corrupt = raw[not_corrupt_mask]
missing_stacks = stacks[not_corrupt_mask]
scores = np.empty(not_corrupt.shape)

for index, missing_stack in enumerate(missing_stacks):
    current_score = 0
    for char in missing_stack[::-1]:
        current_score *= 5
        current_score += score_2[char]
    scores[index] = current_score

scores_sorted = np.sort(scores)
print(f"middle score: {scores_sorted[int(len(scores_sorted)/2)]}")