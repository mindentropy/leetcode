//33. Search in a rotated sorted array.



int search(int *nums, int numsSize, int target)
{
	//Find the point of rotation and then do binary search between the two partitions.
	//Does not make sense as we are doing a first pass which we can as well as search for the value.
	

	for(i = 1; i<numsSize; i++)
	{
		if(nums[i] < min) {
			min = nums;
			min_index = i;
		}
	}

}

int main(int argc, char **argv)
{
	return 0;
}
