#include <stdio.h>
char temp[10000003];
int main(void)
{
	int test_case;
	int T, N, i, res;

	scanf("%d", &T);
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d", &N);
        scanf("%s", temp);
        res = 0;
        i = 0;
        while (temp[i] != '\0')
        {
            if (temp[i] >= '0' && temp[i] <='9')
                res += (temp[i] - '0');
            i++;
        }
		printf("#%d %d\n", test_case, res % (N - 1));
	}
	return 0; 
}