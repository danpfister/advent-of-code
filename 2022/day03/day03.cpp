#include "../Helpers/file_utils.h"
#include <unordered_map>

void part1(std::vector<std::string>& input) {
    int sum = 0;
    for (const auto & backpack : input) {
        std::unordered_map<char, int> items;
        std::string compartment1 = backpack.substr(0, backpack.length()/2);
        std::string compartment2 = backpack.substr(backpack.length()/2, backpack.length()/2);

        for (char item : compartment1) {
            items[item] = 1;
        }
        for (char item : compartment2) {
            if (items.find(item) != items.end()) {
                if (item >= 97 && item <= 122) sum += item - 96;
                else if (item >= 65 && item <= 90) sum += item - 38;
                break;
            }
        }
    }
    
    std::cout << "The sum of the items in both compartments is " << sum << std::endl;
}

void part2(std::vector<std::string> input) {
    int sum = 0;
    for (int i = 0; i < input.size(); i+=3) {
        std::unordered_map<char, int> items1; // items in backpack 1
        std::unordered_map<char, int> items2; // items in backpack 1 and 2
        std::string elf1 = input[i];
        std::string elf2 = input[i+1];
        std::string elf3 = input[i+2];

        for (char item : elf1) {
            items1[item] = 1;
        }
        for (char item : elf2) {
            if (items1.find(item) != items1.end()) {
                items2[item] = 1;
            }
        }
        for (char item : elf3) {
            if (items2.find(item) != items2.end()) {
                if (item >= 97 && item <= 122) sum += item - 96;
                else if (item >= 65 && item <= 90) sum += item - 38;
                break;
            }
        }
    }

    std::cout << "The sum of the badges is " << sum << std::endl;
}

int main() {
    std::vector<std::string> input = FileReader::readFile("C:/Users/Daniel/Github/advent-of-code-2022/day03/input.txt");
    part1(input);
    part2(input);
    return 0;
}