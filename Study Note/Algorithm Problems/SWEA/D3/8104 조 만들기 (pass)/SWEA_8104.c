#include <stdio.h>
int main(void)
{
	int test_case;
	int T, N, K, temp, res, i;
	
	scanf("%d", &T);

	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d %d", &N, &K);
        temp = 0;
        res = 0;
        for (i = 0; i < N / 2; i++)
        {
            res += (temp +  1);
            temp += 2 * K;
            res += temp;
        }
        printf("#%d", test_case);
        if (N % 2)
        {
            res += (temp + 1);
            for (i = 0; i < K; i++)
                printf(" %d", res + i);
        }
        else
            for (i = 0; i < K; i++)
                printf(" %d", res);
        printf("\n");
	}
	return 0; 
}