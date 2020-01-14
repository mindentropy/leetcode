#include <iostream>
#include <vector>

using namespace std;

class Solution {
	public:
		int missingNumber(vector<int> &nums);
};

int Solution::missingNumber(vector<int> &nums)
{
	for(uint32_t i = 0; i<nums.size(); i++) {
		cout<<nums[i]<< " ";
	}
	cout<<"\n";
}

int main(int argc, char **argv)
{
	Solution solution;
	int numvals[] = {3,0,1};

	vector<int> nums(numvals,&numvals[sizeof(numvals)/sizeof(int)]);
	solution.missingNumber(nums);
}
