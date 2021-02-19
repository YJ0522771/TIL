#include <stdio.h>
int main(void)
{
	int test_case;
	int T, N, K, sum, temp, i, j;
	scanf("%d", &T);

	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d %d", &N, &K);
        int score[N];
        for (i = 0; i < N; i++)
            scanf("%d", &score[i]);
        
        for (i = 0; i < N; i++)
            for (j = i + 1; j < N; j++)
				if (score[i] < score[j])
                {
                    temp = score[j];
                    score[j] = score[i];
                    score[i] = temp;
                }
        
        sum = 0;
        for (i = 0; i < K; i++)
            sum += score[i];
        printf("#%d %d\n", test_case, sum);
	}
	return 0;
}