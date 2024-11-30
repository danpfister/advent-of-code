import numpy as np

data = open(r"input.txt", 'r')
inputdata = np.asarray([line.strip() for line in data])[0]

############################## PART 1&2 ##############################

def find_unique_symbols(characters: str, length: int):
    for index in range(len(inputdata)-length+1):
        symbols = [c for c in characters[index:index+length]]
        if np.unique(symbols).shape[0] == length:
            return index+length

if __name__ == "__main__":
    print(f"found packet marker at index {find_unique_symbols(inputdata, 4)}")
    print(f"found message marker at index {find_unique_symbols(inputdata, 14)}")