#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

uint64_t go(uint64_t n, uint64_t acc) {
    if (n <= 1) return acc;
    return go(n-1, n*acc);
}

uint64_t factorial(uint64_t n) {
    return go(n-1, n);
}

int main(int argc, char* argv[]) {
    printf("%llu\n", factorial(strtol(argv[1],NULL,0)));
    return 0;
}

