import numpy as np

file = open(r'input\04.txt', 'r')
lines = [line.strip() for line in file.readlines()]
data_raw = np.asarray(lines)
data = np.delete(data_raw, np.where(data_raw == '', True, False))

############################## PART 1 ##############################

inputdata = data[0].split(",")
data = np.delete(data, 0)

boards = np.empty((100, 5, 5), dtype=np.int32)
for board in range(100):
    for row in range(5):
        index = board * 5 + row
        entries = data[index].split()
        for index, entry in enumerate(entries):
            boards[board][row][index] = entry

masks = np.zeros((100, 5, 5), dtype=bool)
for input in inputdata:
    masks = masks | np.where(boards == int(input), True, False)
    # check if anyone has won
    won = None
    for boardindex, mask in enumerate(masks):
        if np.any(np.all(mask, axis=0) | np.all(mask, axis=1)):
            finalscore = int(input) * np.sum(boards[boardindex][~mask])
            print(f"board {boardindex} has won with finalscore {finalscore}")
            won = True
    if won:
        break

############################## PART 2 ##############################

masks = np.zeros((100, 5, 5), dtype=bool)
hasntwon = np.ones((100), dtype=bool)
for input in inputdata:
    masks = masks | np.where(boards == int(input), True, False)
    # check if anyone has won
    done = None
    for boardindex, mask in enumerate(masks):
        if np.any(np.all(mask, axis=0) | np.all(mask, axis=1)):
            hasntwon[boardindex] = False
        if np.count_nonzero(hasntwon) == 1:
            lastboard = np.argwhere(hasntwon)[0]
        if np.count_nonzero(hasntwon) == 0:
            lastinput = input
            lastboardstate = boards[lastboard][~masks[lastboard]]
            done = True
    if done:
        break

finalscore = int(lastinput) * np.sum(lastboardstate)
print(f"board {lastboard[0]} has finished last with finalscore {finalscore}")