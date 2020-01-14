//415 Add strings
#include <iostream>
#include <string>
#include <sstream>

using namespace std;

class Solution {
public:
	string addStrings(string num1, string num2)
	{
		int sum = 0, carry = 0;
		int i = num1.size();
		int j = num2.size();
		unsigned int maxsize = (i>j)?(i):(j);
		string sumstr(maxsize+1,0); //+1 for carry
		int k = maxsize;

		i--;
		j--;
	
		while((i >=0) && (j >= 0))
		{
			sum = (num1[i] - '0') + (num2[j] - '0') + carry;
			carry = sum / 10;
			sumstr[k--] = (sum%10) + '0';
			i--;
			j--;
		}
	
		while(i>=0) {
			sum = (num1[i] - '0') + carry;
			carry = sum/10;
			sumstr[k--] = (sum%10) + '0';
			i--;
		}

		while(j>=0) {
			sum = (num2[j] - '0') + carry;
			carry = sum/10;
			sumstr[k--] = (sum%10) + '0';
			j--;
		}

		if(carry) {
			sumstr[k--] = carry + '0';
			return sumstr;
		} else {
			return sumstr.substr(1);
		}
	}
};

int main(int argc, char **argv)
{
	Solution sol;
	string teststr = sol.addStrings("0","0");
	cout<<teststr<<endl;
	return 0;
}
