#include <stdio.h>
long long int map[21][2];
int select[21];
int N;

long long int solve(int cur_N, int current)
{
    int i, j;
    long long int temp, local_min = 80000000000, x = 0, y = 0;
    
    if (N / 2 == cur_N)
    {
        for (i = 1; i <= N; i++)
        {
            if (select[i])
            {
                x += map[i][0];
                y += map[i][1];
            }
            else
            {
                x -= map[i][0];
                y -= map[i][1];
            }
        }
        return (x * x) + (y * y);
    }
    
    if (N - current < (N / 2) - cur_N)
        return local_min;
    
    for (i = 1; i <= N - current; i++)
    {
        for (j = 1; j >= 0; j--)
        {
            select[i] = j;
            temp = solve(cur_N + j, current + i);
            if (temp < local_min)
                local_min = temp;
        }
    }
    return local_min;
}

int main(void)
{
	int test_case;
	int T, i;

	scanf("%d", &T);

	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d", &N);
        for (i = 1; i <= N; i++)
            scanf("%lld %lld", &map[i][0], &map[i][1]);
        
        for (i = 1; i <= N; i++)
            select[i] = 0;

        printf("#%d %lld\n", test_case, solve(0, 0));
	}
	return 0;
}