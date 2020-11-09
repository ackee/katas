#include <stdbool.h>
#include <math.h>
#include <stdio.h>

bool is_prime(int num) {
	int limit = num-1;
	if (num > 100) limit = (int)sqrt((double)num);
	if (num <= 1) return false;
	if (num == 2) return true;
	for (int i = (int)sqrt((double)num); i >= 2; --i) {
		if (num % i == 0) return false;	
	}
	return true;
}

int main() {
	for (int i = 0; i < 100; i++) {
		if (is_prime(i)) printf("%d prime? SANT!\n", i);
	}
	return 0;
}
