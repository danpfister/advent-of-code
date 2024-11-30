#include "../Helpers/file_utils.h"
#include <algorithm>

void part1(std::vector<std::string>& input) {
    std::vector<int> calories;
    int current = 0;
    for (const auto & item : input) {
        if (item.size() == 0) {
            calories.push_back(current);
            current = 0;
            continue;
        }
        current += std::stoi(item);
    }
    
    std::sort(calories.begin(), calories.end(), std::greater<int>());

    std::cout << "The elf carrying the most calories is carrying " << calories[0] << " calories." << std::endl;
}

void part2(std::vector<std::string> input) {
    std::vector<int> calories;
    int current = 0;
    for (const auto & item : input) {
        if (item.size() == 0) {
            calories.push_back(current);
            current = 0;
            continue;
        }
        current += std::stoi(item);
    }
    
    std::sort(calories.begin(), calories.end(), std::greater<int>());

    std::cout << "The elves carrying the most calories are carrying " << calories[0] + calories[1] + calories[2] << " calories." << std::endl;
}

int main() {
    std::vector<std::string> input = FileReader::readFile("C:/Users/Daniel/Github/advent-of-code-2022/day01/input.txt");
    part1(input);
    part2(input);
    return 0;
}