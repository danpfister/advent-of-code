import numpy as np
import re

inputfile = open(r"input.txt", 'r')
inputdata = np.asarray([line.strip() for line in inputfile])

class Cpu():
    def __init__(self, interesting_signals: list) -> None:
        self.interesting_signals = interesting_signals
        self.register_value = 1
        self.cycle = 0
        self.interesting_signals_strengths = 0
        self.output = []
    
    def __repr__(self) -> str:
        return f"during cycle {self.cycle} the register value is {self.register_value}"
    
    def next_cycle(self, value: int):
        self.cycle += 1
        if self.cycle in self.interesting_signals:
            self.interesting_signals_strengths += self.cycle * self.register_value # value during cycle
        if self.register_value-1 <= (self.cycle-1)%40 and (self.cycle-1)%40 <= self.register_value+1: # during cycle k, the CRT is drawing on pixel k-1
            self.output.append('#')
        else:
            self.output.append('.')
        if self.cycle%40 == 0:
            self.output.append('\n')
        print(self)
        self.register_value += value

############################## PART 1 ##############################

interesting_signals = [20, 60, 100, 140, 180, 220]
cpu = Cpu(interesting_signals)
for instruction in inputdata:
    if instruction == "noop":
        cpu.next_cycle(0)
        continue
    match = re.match(re.compile(r"addx (-*\d+)"), instruction)
    cpu.next_cycle(0)
    cpu.next_cycle(int(match.group(1)))
print(f"the sum of the interesting signal strengths is {cpu.interesting_signals_strengths}")

############################## PART 2 ##############################

print(''.join(cpu.output))