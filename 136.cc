//136. Single number
#include <iostream>
#include <vector>

using namespace std;

class Solution {

public:
	int singleNumber(vector <int> &nums) {
		
		vector<int>::const_iterator it;
		
		it = nums.begin();
		int num = 0;
		while(it != nums.end()) {
			num ^= *it;
			it++;
		}

		return num;
	}
};

int main(int argc, char **argv)
{
	vector<int> vect;
	Solution solution;

	vect.push_back(1);
	vect.push_back(2);
	vect.push_back(3);
	vect.push_back(2);
	vect.push_back(1);


	cout<<solution.singleNumber(vect)<<endl;


	return 0;
}
