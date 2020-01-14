#include <iostream>
#include <vector>

using namespace std;

class Solution {

public:
	vector<int> nextGreaterElements(vector<int> &nums)
	{
		vector<int> results(nums.size(), -1);
		
		for(int i = 0; i<nums.size(); i++) {
			int j = (i + 1) % nums.size();
			
			while(j != i) {
				if(nums[i] < nums[j]) {
					results[i] = nums[j];
					break;
				}
				j = (j + 1) % nums.size();
			}
		}

		return results;
	}
};

int main(int argc, char **argv)
{
	Solution sol;
	vector<int> nums{1, 2, 1};

	vector<int> results = sol.nextGreaterElements(nums);

	for(auto &num: results) {
		cout<<num<<" ";
	}

	return 0;
}
