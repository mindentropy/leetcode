//4. Median of two sorted arrays
#include <stdio.h>
#include <stdint.h>

double findMedianSortedArrays(
								int *nums1,
								int nums1Size,
								int *nums2,
								int nums2Size
							)
{
	int i = 0;
	int idx1 = 0, idx2 = 0, mid = 0, max = 0;
	int nums[mid = nums1Size+nums2Size];
	
	max = mid >> 1;
	
	for(;((idx1 < nums1Size) || (idx2 < nums2Size))/* && i <= max*/;) {

		while(idx1 < nums1Size) {
			if(idx2 >= nums2Size) {
				nums[i++] = nums1[idx1++];
			} else if(nums1[idx1] < nums2[idx2]) {
				nums[i++] = nums1[idx1++];
			} else if(nums1[idx1] == nums2[idx2]) {
				nums[i++] = nums1[idx1++];
				nums[i++] = nums2[idx2++];
			} else {
				break;
			}
		}

		while(idx2 < nums2Size) {
			if(idx1 >= nums1Size) {
				nums[i++] = nums2[idx2++];
			} else if(nums2[idx2] < nums1[idx1]) {
				nums[i++] = nums2[idx2++];
			} else if(nums1[idx1] == nums2[idx2]) {
				nums[i++] = nums1[idx2++];
				nums[i++] = nums2[idx1++];
				idx1++;
			} else {
				break;
			}
		}
	}

	max = i;
	printf("%d\n",max);
	for(i = 0; i<max; i++) {
		printf("%d ",nums[i]);
	}

	printf("\n");
	//Ignore zero values
	
	if(max & 1) {
		return nums[max/2];
	} else {
		return ((double)nums[max>>1] + (double)nums[(max>>1)-1])/(double)2;
	}

}

int main(int argc, char **argv)
{
	int nums1[] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22};
	int nums2[] = {0,6};

	printf("%f\n",findMedianSortedArrays(nums1, sizeof(nums1)/sizeof(int),
							nums2, sizeof(nums2)/sizeof(int)));
	
}
