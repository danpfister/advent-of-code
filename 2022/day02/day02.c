#include <stdio.h>

#define MAX_LINE_COUNT 2600
#define MAX_LINE_CONTENT 100

void part1(char input[][MAX_LINE_CONTENT], int line_count) {
    int points = 0;
    for (int i = 0; i < line_count; i++) {
        int opponent = input[i][0];
        int me = input[i][2];

        points += me - 87;

        if (me%3 == opponent%3) {
            points += 6;
        } else if (me%3 == (opponent-1)%3) {
            points += 3;
        }
    }

    printf("In the end I will have %d points\r\n", points);
}

void part2(char input[][MAX_LINE_CONTENT], int line_count) {
    int points = 0;
    for (int i = 0; i < line_count; i++) {
        int opponent = input[i][0];
        int outcome = input[i][2];

        int me = 0;
        switch(outcome) {
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

    printf("In the end I will have %d points\r\n", points);
}

int main() {
    char input[MAX_LINE_COUNT][MAX_LINE_CONTENT];
    int line_count = 0;

    FILE* file = fopen("C:/Users/Daniel/Github/advent-of-code-2022/day02/input.txt", "r");
    while (line_count < MAX_LINE_COUNT && fgets(input[line_count], MAX_LINE_CONTENT, file) != NULL) {
        line_count++;
    }
    part1(input, line_count);
    part2(input, line_count);
    return 0;
}