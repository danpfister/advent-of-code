#include <stdio.h>

void part1();
void part2();

int main() {
    part1();
    part2();
    return 0;
}

void part1() {
    char letter;
    int number;

    int current = 50;
    int count = 0;

    FILE *fptr = fopen("input.txt", "r");

    while (fscanf(fptr, " %c%d", &letter, &number) == 2) {
        if (letter == 'L') {
            current = (current + 100 - number)%100;
        } else {
            current = (current + number)%100;
        }
        count += (int)(current == 0);
    }

    fclose(fptr);
    printf("part1 = %d\n", count);
}

void part2() {
    char letter;
    int number;

    int current = 50;
    int count = 0;

    FILE *fptr = fopen("input.txt", "r");

    while (fscanf(fptr, " %c%d", &letter, &number) == 2) {
        if (letter == 'L') {
            for (int i = 0; i < number; i++) {
                current = (current + 99)%100;
                count += (int)(current == 0);
            }
        } else {
            for (int i = 0; i < number; i++) {
                current = (current + 1)%100;
                count += (int)(current == 0);
            }
        }
    }
    
    fclose(fptr);
    printf("part2 = %d\n", count);
}