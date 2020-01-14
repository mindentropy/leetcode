#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char * toLowerCase(char *str)
{
	int i = 0;
	int diff = 0;
	char *resultstr = (char *)malloc(sizeof(char));

	while(str[i] != '\0') {
		if(str[i] >= 'A' && str[i] <= 'Z') {
			diff = str[i] - 'A';
			resultstr[i] = 'a' + diff;
		} else {
			resultstr[i] = str[i];
		}

		resultstr = realloc(resultstr, sizeof(char) + i + 1 + 1);
		i++;
	}

	resultstr[i] = '\0';
	return resultstr;
}

int main(int argc, char **argv)
{
	char *str = "AB";
	char *resultstr;

	printf("Lowercase: %s\n",resultstr =  toLowerCase(str));
	
	free(resultstr);

	return 0;
}
