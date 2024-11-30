#include <file_utils.h>
#include <regex>

void part1(std::vector<std::string>& input) {
    std::regex pattern("(\\d+)-(\\d+),(\\d+)-(\\d+)");
    std::smatch matches;
    int count = 0;

    for (const auto & line : input) {
        if (!std::regex_search(line, matches, pattern)) {
            throw std::runtime_error("no matches found!");
        }
        int start_1 = std::stoi(matches[1]);
        int end_1 = std::stoi(matches[2]);
        int start_2 = std::stoi(matches[3]);
        int end_2 = std::stoi(matches[4]);

        count += ((start_1 <= start_2 && end_1 >= end_2) || (start_1 >= start_2 && end_1 <= end_2));
    }

    std::cout << "the number of pairs where one contains the other is: " << count << std::endl;
}

void part2(std::vector<std::string>& input) {
    std::regex pattern("(\\d+)-(\\d+),(\\d+)-(\\d+)");
    std::smatch matches;
    int count = 0;

    for (const auto & line : input) {
        if (!std::regex_search(line, matches, pattern)) {
            throw std::runtime_error("no matches found!");
        }
        int start_1 = std::stoi(matches[1]);
        int end_1 = std::stoi(matches[2]);
        int start_2 = std::stoi(matches[3]);
        int end_2 = std::stoi(matches[4]);

        count += (start_1 <= end_2 && start_2 <= end_1);
    }

    std::cout << "the number of pairs with overlapt is: " << count << std::endl;
}

int main() {
    std::vector<std::string> input = FileReader::readFile("C:/Users/Daniel/Github/advent-of-code-2022/day04/input.txt");
    part1(input);
    part2(input);
    return 0;
}