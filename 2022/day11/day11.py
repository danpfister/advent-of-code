import numpy as np
import re

class Monkey():
    def __init__(self, number: int, items: list, operation, test_value: int) -> None:
        self.number = number
        self.items = [int(item) for item in items]
        self.number_of_inspects = 0
        self.operation = operation
        self.test_value = test_value
        self.monkey_if_true = None
        self.monkey_if_false = None

    def set_monkeys(self,monkey_if_true, monkey_if_false):
        self.monkey_if_true = monkey_if_true
        self.monkey_if_false = monkey_if_false
    
    def add_item(self, item):
        self.items.append(item)

    def turn(self, part):
        for item in self.items: # inspect items
            self.number_of_inspects += 1
            worry = self.operation(item)
            if part == 1:
                worry //= 3
            if part == 2:
                worry = worry % 9_699_690 # hard-coded LCM of monkeys divisibility tests
            if worry%self.test_value == 0:
                self.monkey_if_true.add_item(worry)
            else:
                self.monkey_if_false.add_item(worry)
        self.items = []

def parse_input(inputdata: list) -> list:
    monkeys = []
    for index in range(0, len(inputdata), 7):
        number = int(re.match(re.compile(r'Monkey (\d+):'), inputdata[index]).group(1))
        items = re.findall(re.compile(r'(?: Starting items: )*(\d+)(?:, )*'), inputdata[index+1])
        operation_match = re.match(re.compile(r'Operation: new = old ([*]|[+]) (old|\d+)'), inputdata[index+2])
        operation = eval(f"lambda old: old {operation_match.group(1)} {operation_match.group(2)}")
        test_value = int(re.match(re.compile(r'Test: divisible by (\d+)'), inputdata[index+3]).group(1))
        monkey_if_true = int(re.match(re.compile(r'If true: throw to monkey (\d+)'), inputdata[index+4]).group(1))
        monkey_if_false = int(re.match(re.compile(r'If false: throw to monkey (\d+)'), inputdata[index+5]).group(1))
        monkeys.append(Monkey(number, items, operation, test_value))
    for index, monkey in zip(range(4, len(inputdata), 7), monkeys):
        monkey_if_true = int(re.match(re.compile(r'If true: throw to monkey (\d+)'), inputdata[index]).group(1))
        monkey_if_false = int(re.match(re.compile(r'If false: throw to monkey (\d+)'), inputdata[index+1]).group(1))
        monkey.set_monkeys(monkeys[monkey_if_true], monkeys[monkey_if_false])
    return monkeys

def round(monkeys, part):
    for monkey in monkeys:
        monkey.turn(part)

if __name__ == "__main__":
    inputfile = open(r"input.txt", 'r')
    inputdata = np.asarray([line.strip() for line in inputfile])
    ############################## PART 1 ##############################
    monkeys = parse_input(inputdata)
    for round_number in range(20):
        round(monkeys, part=1)
    number_of_inspects_all = [monkey.number_of_inspects for monkey in monkeys]
    number_of_inspects_all.sort(reverse=True)
    print(f"the level of monkey business is {number_of_inspects_all[0] * number_of_inspects_all[1]}")
    ############################## PART 2 ##############################
    monkeys = parse_input(inputdata)
    for round_number in range(10000):
        round(monkeys, part=2)
    number_of_inspects_all = [monkey.number_of_inspects for monkey in monkeys]
    number_of_inspects_all.sort(reverse=True)
    print(f"the level of monkey business is {number_of_inspects_all[0] * number_of_inspects_all[1]}")