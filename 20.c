//20. Valid Parenthesis
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

char stk_pop(char *stk, int32_t *stk_idx)
{
	return stk[--(*stk_idx)];
}

void stk_push(char *stk, int32_t *stk_idx, uint32_t ch)
{
	stk[(*stk_idx)++] = ch;
}

int isValid(char *s)
{
	char stk[strlen(s)], ch;
	int32_t stk_idx = 0, i = 0;

	while(s[i] != '\0')
	{
		if((s[i] == '{') || (s[i] == '[') || (s[i] == '('))
			stk_push(stk, &stk_idx, s[i]);
		else if( ((s[i] == '}') || (s[i] == ']') || (s[i] == ')')) ){
			
			if(stk_idx == 0)
				return -1;

			ch = stk_pop(stk, &stk_idx);

			
			if(s[i] == '}' && ((ch == '[') || (ch == '(')) )
				return -1;
			else if(s[i] == ']' && ((ch == '{') || (ch == '(')) )
				return -1;
			else if(s[i] == ')' && ((ch == '{') || (ch == '[')) )
				return -1;
		}
		i++;
	}

	if(stk_idx == 0)
		return 0;
	else 
		return -1;
}


int main(int argc, char **argv)
{
	char teststr[] = "([)]";

	printf("Is valid : %d\n", isValid(teststr));

	return 0;
}
