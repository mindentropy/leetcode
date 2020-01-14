#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

#define INT_ARR_SIZE(numarr) \
	sizeof(numarr)/sizeof(int)

int bin_search(int *nums, int val, int size)
{
	int low = 0, high = size - 1;
	int mid = 0;

	while(low <= high) {
		mid = (low+high) >> 1;

		if(nums[mid] == val) {
			return mid;
		} else if(nums[mid] > val) {
			high = mid - 1;
		} else if(nums[mid] < val) {
			low = mid + 1;
		}
	}

	return -1;
}

int * searchRange(int *nums, int numsSize, int target, int *returnSize)
{
	int idx = 0;
	int min = 0, max = 0;
	int *return_range = malloc(sizeof(int) << 1);
	*returnSize = 2;

	idx = bin_search(nums, target, numsSize);
	
	if(idx == -1) {
		return_range[0] = return_range[1] = -1;
		return return_range;
	}
		
	min = max = idx;
	
	while((nums[min] == target) && min >=0) {
		min--;
	}
	min++;

	while((nums[max] == target) && max < numsSize) {
		max++;
	}
	max--;

	return_range[0] = min;
	return_range[1] = max;

	return return_range;
}

int main(int argc, char **argv)
{
	int nums[] = {0, 0, 0, 1, 2, 3};
	int returnSize = 0, i = 0;

/*	int idx = bin_search(nums, 8, INT_ARR_SIZE(nums));
	printf("%d\n", idx);*/
	int *range = searchRange(nums,INT_ARR_SIZE(nums),
							0,&returnSize);

	for(i = 0; i<returnSize; i++) {
		printf("%d ",range[i]);
	}

	printf("\n");
}
