#include <stdio.h>
int main(void)
{
	int test_case;
	int T, N, res, temp, i;
	
	scanf("%d", &T);
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d", &N);
        res = 0;
        for (i = 0; i < N; i++)
        {
            scanf("%d", &temp);
            if (res + temp >= res * temp)
                res += temp;
            else
                res *= temp;
        }
        printf("#%d %d\n", test_case, res);
	}
	return 0;
}