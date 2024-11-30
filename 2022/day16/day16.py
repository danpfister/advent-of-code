import numpy as np
import re
import time

def parse_input(inputdata: list):
    valves = dict()
    for line in inputdata:
        match_all = re.match(re.compile(r'Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.+)'), line)
        match_connected = re.findall(re.compile(r'(\w+)'), match_all.group(3))
        valves[match_all.group(1)] = {
            'flow_rate':    int(match_all.group(2)),
            'connected':    match_connected
        }
    return valves

def release_pressure(valves: dict, current_valve: str, time_left: int, pressure_released: int, open_valves: list):
    if time_left == 0:
        return pressure_released
    if len(open_valves) == 15:
        return pressure_released
    if valves[current_valve]['flow_rate'] == 0 or current_valve in open_valves:
        return max([release_pressure(valves, next_valve, time_left-1, pressure_released, open_valves) for next_valve in valves[current_valve]['connected']])
    else:
        open_valve = release_pressure(valves, current_valve, time_left-1, pressure_released+(time_left-1)*valves[current_valve]['flow_rate'], open_valves + [current_valve])
        move_next = max([release_pressure(valves, next_valve, time_left-1, pressure_released, open_valves) for next_valve in valves[current_valve]['connected']])
        return max(open_valve, move_next)
        

if __name__ == "__main__":
    inputfile = open(r"input.txt", 'r')
    inputdata = np.asarray([line.strip() for line in inputfile])
    valves = parse_input(inputdata)
    non_zero_valves = len([v for v in valves if valves[v]['flow_rate'] != 0])
    start = time.time()
    print(release_pressure(valves, 'AA', 30, 0, []))
    print(f"running the recursive implementation took {time.time() - start} seconds")