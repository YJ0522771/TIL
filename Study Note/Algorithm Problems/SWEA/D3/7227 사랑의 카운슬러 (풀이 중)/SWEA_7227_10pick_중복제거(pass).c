#include <stdio.h>
long long int map[21][2];
int select[21];
int N;
long long int res;

void solve(int cur_N, int current)
{
    int i;
    long long int temp, x, y;

    if (current > N)
        return;
    
    if (N / 2 == cur_N)
    {
        x = 0;
        y = 0;
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
        temp = (x * x) + (y * y);
        if (res > temp)
            res = temp;
        return;
    }
    
    for (i = 1; i >= 0; i--)
    {
        select[current + 1] = i;
        solve(cur_N + i, current + 1);
    }
    return;
}

int main(void)
{
	int test_case;
	int T, i, j;

	scanf("%d", &T);

	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d", &N);
        for (i = 1; i <= N; i++)
            scanf("%lld %lld", &map[i][0], &map[i][1]);
        
        for (i = 1; i <= N; i++)
            select[i] = 0;
		res = 80000000000;
        solve(0, 0);
        printf("#%d %lld\n", test_case, res);
	}
	return 0;
}