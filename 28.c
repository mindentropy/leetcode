#include <stdio.h>
#include <stdint.h>

int strStr(char *haystack, char *needle)
{
	uint32_t i = 0, j = 0, k = 0;

	if((haystack[0] == '\0') && (needle[0] == '\0'))
		return 0;

	while(haystack[i] != '\0')
	{
		j = i, k = 0;
		while(1) {
			if(needle[k] == '\0')
				return i;

			if(haystack[j] != needle[k])
				break;

			if(haystack[j] == '\0')
				return -1; //End of the string.

			j++;
			k++;
		}
		i++;
	}
	return -1;
}

int main(int argc, char **argv)
{
	char str[] = "TEST";	
	char substr[] = "ES";

	printf("Index : %d\n", strStr(str,substr));
}
