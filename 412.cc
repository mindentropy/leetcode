#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;


class Solution {
public:
	vector <string> fizzBuzz(int n)
	{
		vector <string> fbstr;
		fbstr.resize(n);

		for(int i = 1; i<=n; i++)
		{
			if(((i%3) == 0) && ((i%5) == 0)) {
				fbstr[i-1] = string("FizzBuzz");
			} else if((i%3) == 0) {
				fbstr[i-1] = string("Fizz");
			} else if((i%5) == 0) {
				fbstr[i-1] = string("Buzz");
			} else {
				stringstream ss;
				ss<<i;
				fbstr[i-1] = ss.str();
			}
		}
		return fbstr;
	}
};

int main(int argc, char **argv)
{
	int n = 15;
	Solution solution;
	vector<string> fbstr = solution.fizzBuzz(n);

	for(int i = 1; i<=n; i++)
	{
		cout<<fbstr[i-1]<<endl;
	}
	return 0;
}
