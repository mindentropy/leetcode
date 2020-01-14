#include <stdio.h>
#include <stdint.h>
#include <limits.h>

#define VAL_CHK (INT_MAX/10)

int myAtoi(char* str) {
	int32_t num = 0,i = 0;
	int neg_flag = 0;
	int tmp_val = 0;

/*
 * 1) Discard as many whitespace characters as possible
 * 2) If non whitespace character then check for optional '+' or '-'
 * 3) Check for overflow.
 */


	//Eat all the whitespace characters
	while(str[i]  == ' ')
		i++;
	
	if((str[i] == '-') || (str[i] == '+')) {
		if(str[i] == '-')
			neg_flag = 1;
		i++;
	}

	while(str[i] != '\0') {

		if(((str[i] - '0') < 0)  || ((str[i] - '0') > 9))
			break;
		
		if(num > VAL_CHK) {

			if(neg_flag == 0)
				return INT_MAX;

			if(neg_flag == 1)
				return INT_MIN;
		}

		num *= 10;

		if( num > (INT_MAX - (str[i] - '0')) ) {

			if(neg_flag == 0)
				return INT_MAX;

			if(neg_flag == 1)
				return INT_MIN;
		}
		
		num += (str[i] - '0');

/*		
		if(neg_flag == 0 && (num < 0))
			return INT_MAX;

		if(neg_flag == 1 && num < 0)
			return INT_MIN;
*/
		i++;
	}

	return (neg_flag)?(-num):(num);

}

int main(int argc, char **argv)
{
	char numstr[] = "10522545459";

	int val = myAtoi(numstr);

	printf("%d\n",val);
	
	return 0;
}
