//621. Task scheduler
#include <iostream>
#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    int leastInterval(vector<char>& tasks, int n);
};

int Solution::leastInterval(vector <char> &tasks, int n)
{
	map<char, int> taskmap;
	for(int i = 0; i<tasks.size(); i++) {
		taskmap[tasks[i]]++;
	}
	cout<<"count :"<<taskmap['A']<<endl;
	cout<<"count :"<<taskmap['B']<<endl;

	return 0;
}

int main(int argc, char **argv)
{
	vector <char> tasks = {'A','A','A','B','B','B'};
	int n = 2;

	Solution solution;

	cout<<"CPU Intervals : "<<solution.leastInterval(tasks,n)<<endl;
	
	return 0;
}
