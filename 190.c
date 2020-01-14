//190. Reverse Bits
#include <stdio.h>
#include <stdint.h>

#define swap_bits(n,idx1,idx2) \
	(((n & (1<<idx1))>>idx1) != ((n & (1<<idx2))>>idx2)?(n ^ ((1<<idx1) | (1<<idx2))):n)

/*
uint32_t swap_bits(uint32_t n, int idx1, int idx2)
{
	if((n & (1<<idx1)) != (n & (1<<idx2))) {
		n = n ^ ((1<<idx1)|(1<<idx2));
	}
	return n;
}
*/
uint32_t reverseBits(uint32_t n)
{
	uint32_t i = 0;
	while(i<16) {
		n = swap_bits(n,i,31-i);
		i++;
	}
	return n;
}

int main(int argc, char **argv)
{
	uint32_t x = 43261596;

	printf("%u\n",reverseBits(x));
}
