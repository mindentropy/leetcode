//344. Reverse string
#include <iostream>
#include <string>

using namespace std;

class Solution {

public:
	string reverseString(string s)
	{
		int i = 0;
		int j = s.size()-1;
		char tmp;

		while(i < j) {
			tmp = s[i];
			s[i] = s[j];
			s[j] = tmp;
			i++;
			j--;
		}
		return s;
	}
};

int main(int argc, char **argv)
{
	Solution solution;
	cout<<solution.reverseString("hello");

	return 0;
}
