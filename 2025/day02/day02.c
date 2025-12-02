#include <stdio.h>
#include <math.h>

int get_digit_count(long long number) {
    int count = 0;
    while (number > 0) {
        number /= 10;
        count++;
    }
    return count;
}

void part1() {
    long long start, end;
    long long invalids = 0;
    int a, b;
    FILE *fptr;
    fptr = fopen("input.txt", "r");

    while (fscanf(fptr, "%lld-%lld%*c", &start, &end) >= 2) {
        printf("%lld - %lld ", start, end);

        int digits = get_digit_count(start);
        if (digits%2 != 0) {
            start = pow(10, digits) + pow(10, digits/2);
            printf("adjusted ");
        } else {
            a = start / pow(10, digits/2);
            b = start % (int)pow(10, digits/2);
            if (a > b) {
                start = a * pow(10, digits/2) + a;
            } else if (a < b) {
                a++;
                start = a * pow(10, digits/2) + a;
            }
            // if a == b, do nothing
        }

        if (start > end) continue;

        while (start <= end) {
            invalids += start;
            digits = get_digit_count(start);
            start += pow(10, digits/2) + 1;

            // this part is necessary because of behaviour at places like 99
            digits = get_digit_count(start);
            if (digits%2 != 0) {
                start = pow(10, digits) + pow(10, digits/2);
            }
            printf(" %d", start);
        }

        printf("\n");
    }

    fclose(fptr);
    printf("invalids: %lld\n", invalids);
}

int main() {
    part1();
    return 0;
}