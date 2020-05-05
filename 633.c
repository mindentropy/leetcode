#include <stdio.h>
#include <stdbool.h>

bool judgeSquareSum(int c)
{
	long a = 0;
	long b = 0;

	long tmpa = 0;
	long tmpb = 0;
	while((tmpa = (a * a)) <= c) {
		b = a;

		while((tmpb = (b * b)) <= c) {
			if((tmpa + tmpb) == c)
				return true;
			b += 1;
		}
		a += 1;
	}

	return false;
}


int main(int argc, char **argv)
{
	printf("%s", judgeSquareSum(2147482647) ? "true": "false");
	return 0;
}
