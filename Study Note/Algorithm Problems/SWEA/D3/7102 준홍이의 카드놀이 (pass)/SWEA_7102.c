#include <stdio.h>
int main(void)
{
	int test_case;
	int T, N, M, i, K;
	
	scanf("%d", &T);
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d %d", &N, &M);
        if (N > M)
        {
            K = N - M;
        	N = M;
        }
        else
        	K = M - N;
        printf("#%d", test_case);
        for (i = 0; i <= K; i++)
            printf(" %d", N + i + 1);
        printf("\n");
	}
	return 0;
}