#include <stddef.h>
#include <stdio.h>

size_t countBits(unsigned long value);

int main() {
	unsigned long v = 0b1001001011010000111101;
	printf("%lu ettor!\n", countBits(v));
	return 0;
}

size_t countBits(unsigned long value) {
	size_t ones = 0;  
	unsigned long check = 1;
	for (int i = 0; i < 32; i++) { /* Set a max of 32 bits. */
		if ((check << i) & value) ones++;
	}
	return ones;

}
