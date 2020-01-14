#include <iostream>
#include <string>
//#include <stdint>

using namespace std;

class Solution {
	public:
		int strStr(string haystack, string needle);
};

int Solution::strStr(string haystack, string needle)
{
	uint32_t i = 0, j = 0, k = 0;

	if((haystack[i] == '\0') && (needle[j] == '\0'))
		return 0;
	
	while(haystack[i] != '\0') {
		j = i,k = 0;

		while(1) {

			if(needle[k] == '\0')
				return i;

			if(haystack[i] == '\0')
				return -1;

			if(haystack[j] != needle[k])
				break;
		
			j++;
			k++;
		}
		i++;
	}

	return -1;
}

int main(int argc, char **argv)
{
	Solution solution;

	cout<<"Index : "<<solution.strStr("TEST","ES")<<"\n";

	return 0;
}
