#include <iostream>

using namespace std;


/*
 * I will first take a simple example:
 *
 * m = 00000
 *     00001
 *     00010
 *     00011
 *     00100
 *     00101
 *     00110
 *     00111
 * n = 01000
 * 
 * 1) I find that if m != n then the lowest bit position
 *    changes its value from 0 to 1 or 1 to 0. Hence the AND operation when
 *    of the lowest bit position will be 0.
 * 2) In case of m == n the lowest bit position does not change. Therefore in this
 *    case the AND operation will yield 1.
 * 
 * In other words for the range [m,n] where n > m the lowest bit position will
 * always be 0. If the lowest bit of m is 0 or 1 then the lowest bit of m AND m+1
 * must be 0.
 *
 * We got the lowest bit for the final result. Next we have to check for the 2nd
 * lowest bit. We can simply bit shift m and n by 1 i.e. m>>1 and n>>1
 *
 * When to stop looping?
 * ====================
 *
 * Consider
 * m = 01000
 * n = 01011
 *
 * (1) 01011 > 01000 --> lowest bit = 0
 * (2) 0101 > 0100 --> lowest bit = 0
 * (3) 010 = 010 --> lowest bit = 0
 * (4) 01 = 01 --> lowest bit = 1
 * (5) 0 = 0 -- > lowest bit = 0
 *
 * Final result --> 01000
 *
 * We can see from the result that steps (3) and (5) are unnecessary, when m=n
 * as the bits are the same for m and n.
 */
 
class Solution {
public:
	int rangeBitwiseAnd(int m, int n)
	{
		int shiftcnt = 0;

		while(n>m) {
			m >>= 1;
			n >>= 1;
			shiftcnt++;
		}

		return m<<shiftcnt;
		
//		for(ans = m, i = m + 1; i<=n; i++) {
//			ans = ans & i;
//		}

//		return ans;
	}
};

int main(int argc, char **argv)
{
	Solution solution;


	printf("%d\n",solution.rangeBitwiseAnd(5,7));

	return 0;
}
