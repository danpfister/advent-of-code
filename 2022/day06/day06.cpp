#include <file_utils.h>
#include <cstdint>
#include <bit>

int findUniqueValues(std::string buffer, int windowSize) {
    std::uint32_t values = 0;
    int currentIndex = 0;
    // iterate until there are 4 ones in the binary representation of the window
    while (std::popcount(values) != windowSize) {
        std::string window =  buffer.substr(currentIndex, windowSize);
        values = 0;
        for (const int & symbol : window) {
            // each letter gets mapped to a different position in the 32bit int
            std::uint32_t values_before = values;
            values |= 0b1 << (symbol - 97);
            // break if nothing changed (i.e. we added a value which already was in the 32bit int)
            // should lead to a tiny speedup
            if (values_before == values) {
                break;
            }
        }
        currentIndex++;
    }

    return currentIndex + windowSize - 1;
}

void part1(std::vector<std::string> input) {
    std::cout << "The location of the marker is at: " << findUniqueValues(input[0], 4) << std::endl;
}

void part2(std::vector<std::string> input) {
    std::cout << "The location of the marker is at: " << findUniqueValues(input[0], 14) << std::endl;
}

int main() {
    std::vector<std::string> input = FileReader::readFile("C:/Users/Daniel/Github/advent-of-code-2022/day06/input.txt");

    part1(input);
    part2(input);

    return 0;
}