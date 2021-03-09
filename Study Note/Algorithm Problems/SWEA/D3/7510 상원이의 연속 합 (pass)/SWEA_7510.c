#include <stdio.h>
int main(void)
{
	int test_case;
	int T, N, i, j, temp, count;
	
	scanf("%d", &T);
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d", &N);
        count = 0;
		for (i = 1; i <= N; i++)
        {
            temp = 0;
            for (j = i; j <= N; j++)
            {
            	temp += j;
                if (temp == N)
                {
                    count++;
                    break;
                }
                else if (temp > N)
                    break;
            }
        }
        printf("#%d %d\n", test_case, count);
	}
	return 0;
}