#include <stdio.h>
char a[100][10];
long int cost[100];
char b[1000][10];
int main(void)
{
	int test_case;
	int T, N, M, i, j, k, state;
    long int res;
	
	scanf("%d", &T);
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d %d", &N, &M);
        for (i = 0; i < N; i++)
        {
            scanf("%s", a[i]);
            //printf("%s ", a[i]);
            scanf("%ld", &cost[i]);
            //printf("%d\n", cost[i]);
        }
        for (i = 0; i < M; i++)
            scanf("%s", b[i]);
        
        res = 0;
        for (i = 0; i < N; i++)
            for (j = 0; j < M; j++)
            {
                state = 1;
                for (k = 0; k < 8; k++)
                    if (a[i][k] != '*' && a[i][k] != b[j][k])
                    {
                        state = 0;
                        break;
                    }
                if (state)
                    res += cost[i];
            }
		printf("#%d %ld\n", test_case, res);      
	}
	return 0;
}