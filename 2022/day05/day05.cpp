#include <file_utils.h>
#include <regex>
#include <iterator>

struct Instruction {
    int amount;
    int origin;
    int destination;
};

void parse_input(std::vector<std::string>& input, std::vector<Instruction>& instructions, std::vector<std::stack<char>>& initialStacks) {
    std::vector<std::pair<int, int>> indicesPairs = {{0, 1}, {1, 5}, {2, 9}, {3, 13}, {4, 17}, {5, 21}, {6, 25}, {7, 29}, {8, 33}}; 

    std::vector<std::string> stackLines(input.begin(), input.begin() + 8);
    std::vector<std::string> instructionsLines(input.begin() + 10, input.end());
    std::regex pattern("move (\\d+) from (\\d+) to (\\d+)");
    std::smatch matches;

    // parse initial stack layout
    for (auto  it = stackLines.rbegin(); it != stackLines.rend(); it++) {
        auto line = *it;
        for (const auto & pair : indicesPairs) {
            if (line[pair.second] != ' ') {
                initialStacks[pair.first].emplace(line[pair.second]);
            }
        }
    }

    // parse instructions
    for (const auto & line : instructionsLines) {
        if (!std::regex_search(line, matches, pattern)) {
            throw std::runtime_error("no matches found!");
        }
        int amount = std::stoi(matches[1]);
        int origin = std::stoi(matches[2]) - 1;
        int destination = std::stoi(matches[3]) - 1;

        instructions.emplace_back(Instruction{amount, origin, destination});
    }
}

void part1(std::vector<std::string>& input, std::vector<Instruction>& instructions, std::vector<std::stack<char>> stacks) {
    for (const auto & instruction : instructions) {
        for (int i = 0; i < instruction.amount; i++) {
            char crate = stacks[instruction.origin].top();
            stacks[instruction.destination].push(crate);
            stacks[instruction.origin].pop();
        }
    }

    std::string output;
    for (const auto & stack : stacks) {
        output += stack.top();
    }
    std::cout << "The top crates are: " << output << std::endl;
}

void part2(std::vector<std::string>& input, std::vector<Instruction>& instructions, std::vector<std::stack<char>> stacks) {
    for (const auto & instruction : instructions) {
        std::stack<char> temp;
        for (int i = 0; i < instruction.amount; i++) {
            char crate = stacks[instruction.origin].top();
            temp.push(crate);
            stacks[instruction.origin].pop();
        }
        while (!temp.empty()) {
            char crate = temp.top();
            stacks[instruction.destination].push(crate);
            temp.pop();
        }
    }

    std::string output;
    for (const auto & stack : stacks) {
        output += stack.top();
    }
    std::cout << "The top crates are: " << output << std::endl;
}

int main() {
    std::vector<std::string> input = FileReader::readFile("C:/Users/Daniel/Github/advent-of-code-2022/day05/input.txt");
    std::vector<Instruction> instructions;
    std::vector<std::stack<char>> initialStacks(9);

    parse_input(input, instructions, initialStacks);

    part1(input, instructions, initialStacks);
    part2(input, instructions, initialStacks);

    return 0;
}