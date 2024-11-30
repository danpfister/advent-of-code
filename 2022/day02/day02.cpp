#include "../Helpers/file_utils.h"
#include <algorithm>

void part1(std::vector<std::string>& input) {
    int points = 0;
    for (const auto & turn : input) {
        int opponent = (int)turn[0];
        int me = (int)turn[2];

        points += me - 87; // points according to shape chosen

        if (me%3 == opponent%3) {
            // I won
            points += 6;
        } else if (me%3 == (opponent-1)%3) {
            // draw
            points += 3;
        } // else loss -> no points
    }
    std::cout << "In the end I will have " << points << " points" << std::endl;;
}

void part2(std::vector<std::string> input) {
    int points = 0;
    for (const auto & turn : input) {
        int opponent = (int)turn[0];
        int outcome = (int)turn[2];

        int me = 0;
        switch (outcome)
        {
        case 88: // loss
            me = (opponent-2)%3+87;
            me = (me == 87) ? 90 : me; // ugly fix for scissors getting mapped to 87 instead of 90
            break;
        case 89: // draw
            points += 3;
            me = (opponent-1)%3+87;
            me = (me == 87) ? 90 : me;
            break;
        case 90: // win
            points += 6;
            me = opponent%3+87;
            me = (me == 87) ? 90 : me;
            break;
        }
        points += me - 87;
    }
    std::cout << "In the end I will have " << points << " points" << std::endl;
}

int main() {
    std::vector<std::string> input = FileReader::readFile("C:/Users/Daniel/Github/advent-of-code-2022/day02/input.txt");
    part1(input);
    part2(input);
    return 0;
}