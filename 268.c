#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int missingNumber(int *nums, int numsSize)
{
	uint32_t sum = 0, a_sum = 0;
	uint32_t i = 0;
	uint32_t min = 0, max = 0;

	max = nums[i];
	
	min = 0;

	for(i = 0; i<numsSize; i++) {

		if(nums[i] > max) 
			max = nums[i];

		sum += nums[i];
	}

	for(i = min; i<(min+numsSize+1); i++) {
		a_sum += i;
	}

	return a_sum - sum;
}

int main(int argc, char **argv)
{
	int nums[] = {0};

	printf("%u\n",missingNumber(nums,sizeof(nums)/sizeof(int)));

	return 0;
}
