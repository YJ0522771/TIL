#include <stdio.h>
char num[100002];

int main(void)
{
	int test_case;
	int T, len, i;
	
	scanf("%d", &T);
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%s", num);
        // printf("%s\n", num);
        
        i = 0;
        while (num[i] != '\0')
        	i++;
        len = i;
        
        printf("#%d ", test_case);
        if (num[0] == '9' && num[1] == '9' && num[2] >= '5')
            printf("1.0*10^%d\n", len);
        else if (num[1] == '9' && num[2] >= '5')
            printf("%d.0*10^%d\n", num[0] - '0' + 1, len - 1);
        else if (num[2] >= '5')
            printf("%d.%d*10^%d\n", num[0] - '0', num[1] - '0' + 1, len - 1);
        else
            printf("%d.%d*10^%d\n", num[0] - '0', num[1] - '0', len - 1);
	}
	return 0; 
}