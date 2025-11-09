#include <stdio.h>

typedef signed long long int64_t;

int64_t max_range = 100000;

int main(int argc, char** argv) {
    int64_t count = 0;

    for (int64_t dividend = 1; dividend < max_range + 1; dividend++) {

        int is_prime = 1;
        for (int64_t divisor = 2; divisor < dividend; divisor++) {
            if (dividend % divisor == 0)  {
                is_prime = 0;
                break;
            }
        }

        if (!is_prime) {
            continue;
        }
        count++;

    }
    printf("%llu\n", count);
}