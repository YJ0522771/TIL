#include <stdio.h>
int main(void)
{
	int test_case;
	int T, N, M, i, j, max, count, temp, sum;
	
	scanf("%d", &T);
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d %d", &N, &M);
        max = 0;
        count = 0;
        for (i = 0; i < N; i++)
        {
            sum = 0;
            for (j = 0; j < M; j++)
            {
                scanf("%d", &temp);
                sum += temp;
            }
            if (max < sum)
            {
                max = sum;
                count = 1;
            }
            else if (max == sum)
                count++;
        }
		printf("#%d %d %d\n", test_case, count, max);
	}
	return 0;
}