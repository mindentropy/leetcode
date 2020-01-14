//455 -- Assign cookies
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {

public:
	int findContentChildren(vector<int> &g, vector<int> &s);
};

int Solution::findContentChildren(vector<int> &g, vector<int> &s)
{
	int gr = 0;
	int sz = 0;
	
	if(s.size() == 0 || g.size() == 0)
		return 0;

	sort(g.begin(), g.end());
	sort(s.begin(), s.end());

	while(gr<g.size() && sz<s.size())
	{
		if(g[gr] <= s[sz])
		{
			gr++;
		} 
		sz++;
	}
	return gr;
}


int main(int argc, char **argv)
{
	Solution solution;

	vector <int> g = {10,9,8,7};
	vector <int> s = {10,9,8,7};

	cout<<"Maximum satisfied children : "<<solution.findContentChildren(g,s)<<endl;

	return 0;
}
