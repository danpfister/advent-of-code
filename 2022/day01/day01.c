#include <stdio.h>
#include <stdlib.h>

void part1(char input[][100], int line_count) {
    int best = 0;
    int current = 0;
    for (int i = 0; i < line_count; i++) {
        if (input[i][0] == '\n') {
            if (current > best) best = current;
            current = 0;
            continue;
        }
        current += strtol(input[i], NULL, 10);
    }

    printf("The elf carrying the most calories is carrying %d calories\r\n", best);
}

void part2(char input[][100], int line_count) {
    int best[3] = {0, 0, 0};
    int current = 0;
    for (int i = 0; i < line_count; i++) {
        if (input[i][0] == '\n') {
            if (current > best[0]) {
                best[2] = best[1];
                best[1] = best[0];
                best[0] = current;
            } else if (current > best[1]) {
                best[2] = best[1];
                best[1] = current;
            } else if (current > best[2]) {
                best[2] = current;
            }
            current = 0;
            continue;
        }
        current += strtol(input[i], NULL, 10);
    }
    
    printf("The elves carrying the most calories are carrying %d calories\r\n", best[0] + best[1] + best[2]);
}

int main() {
    char input[2500][100];
    int line_count = 0;

    FILE* file = fopen("C:/Users/Daniel/Github/advent-of-code-2022/day01/input.txt", "r");
    while (line_count < 2500 && fgets(input[line_count], 100, file) != NULL) {
        line_count++;
    }
    part1(input, line_count);
    part2(input, line_count);
    return 0;
}