//405 -- Convert a number to hexadecimal
//
//1. All letters in hexadecimal (a-f) must be in lowercase.
//2. The hexadecimal string must not contain extra leading 0s. 
//   If the number is zero, it is represented by a single zero character '0'; 
//   otherwise, the first character in the hexadecimal string will not be the 
//   zero character.
//3. The given number is guaranteed to fit within the range of a 32-bit signed 
//   integer.
//4. You must not use any method provided by the library which converts/formats 
//   the number to hex directly.

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

char * toHex(uint32_t val)
{
	uint32_t i = 0, j = 0;
	uint32_t tmpval = 0;
	char *strbuff = malloc(9);

	while(!(val & 0xF0000000) && (i<8)) {
		val <<= 4;
		i++;
	}

	for(;i<8; i++) {
		tmpval = (val & 0xF0000000)>>28;
		val = val << 4;

		if((tmpval < 10)) {
			strbuff[j++] = '0' + tmpval;
		} else {
			strbuff[j++] = 'a' + tmpval - 10;
		}
	}

	if(j)
		strbuff[j] = '\0';
	else {
		strbuff[j++] = '0';
		strbuff[j] = '\0';
	}

	return strbuff;
}

int main(int argc, char **argv)
{
	//uint32_t val = 2864434397;
	uint32_t val = 16;
	char *str;
	str = toHex(val);

	printf("0x%s\n",str);

	return 0;
}
