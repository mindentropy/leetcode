//27 -- Remove Element
#include <stdio.h>
#include <stdint.h>

int removeElement(int *nums, int numsize, int val)
{
	int i = 0, j = 0;

	for(i = 0; i<numsize; i++) {
		if(nums[i] != val) {
			nums[j++] = nums[i];
		}
	}

	return j;
}

int main(int argc, char **argv)
{
	int nums[] = {2, 2, 2, 2};
	int elements = 0, i = 0;

	elements = removeElement(nums, sizeof(nums)/(sizeof(int)), 3);

	for(i = 0; i<elements; i++) {
		printf("%d ", nums[i]);
	}
	printf("\n");

	return 0;
}
