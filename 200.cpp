//200 Number of islands

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
	int numIslands(vector<vector<char>> &grid);
};

int Solution::numIslands(vector<vector<char>> &grid)
{
	int rows = grid.size();
	if(rows == 0)
		return 0;
	int cols = grid[0].size();
	int num_of_islands = 0;

	//Find a root note which can trigger a BFS.
	//This means find a 1 push the row,col onto the queue 
	//and set the row,col to 0. Push the neighbours onto the
	//queue and we start with these neighbours in the next iteration.
	for(int i = 0; i<rows; i++){
		for(int j = 0; j<cols; j++)
		{
			if(grid[i][j] == '1') {
				num_of_islands++;
				grid[i][j] = '0';
				
				queue<pair<int,int>> neighbours;
				neighbours.push({i,j});

				while(!neighbours.empty())
				{
					auto rc = neighbours.front();
					neighbours.pop();

					int row = rc.first; int col = rc.second;

					if((row - 1) >= 0 && grid[row - 1][col] == '1')
					{
						grid[row-1][col] = '0';
						neighbours.push({row-1,col});
					}

					if((row + 1) < rows && grid[row + 1][col] == '1')
					{
						grid[row+1][col] = '0';
						neighbours.push({row + 1,col});
					}

					if((col - 1) >= 0 && grid[row][col - 1] == '1')
					{
						grid[row][col - 1] = '0';
						neighbours.push({row,col - 1});
					}

					if((col + 1) < cols && grid[row][col + 1] == '1')
					{
						grid[row][col + 1] = '0';
						neighbours.push({row,col + 1});
					}
				}
			}
		}
	}

	return num_of_islands;
}

int main(int argc, char **argv)
{
	Solution solution;
	vector<vector<char>> grid;

	grid.push_back({'1','1','1','1','0'});
	grid.push_back({'1','1','0','1','0'});
	grid.push_back({'1','1','0','0','0'});
	grid.push_back({'0','0','0','0','0'});

	cout<<"Num of islands: "<<solution.numIslands(grid);
	cout<<"\n";

	return 0;
}
