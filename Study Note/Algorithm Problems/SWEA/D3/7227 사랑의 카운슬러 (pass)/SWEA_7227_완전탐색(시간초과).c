#include <stdio.h>
long long int map[21][2];
int visit[21];
int N;

long long int solve(int cur_N, long long int del_x, long long int del_y)
{
    int i,j, from, to;
    long long int temp, local_min, x, y;
    local_min = 80000000000;
    
    if (N == cur_N)
    {
        temp = (del_x * del_x) + (del_y * del_y);
        return temp;
    }
    
    for (i = 1; i <= N; i++)
        if (!visit[i])
            break;
    from = i;
    visit[from] = 1;
    
    for (to = 1; to <= N; to++)
    {
        if (to == from)
            continue;
        
        if (!visit[to])
        {
            visit[to] = 1;
            
            x = map[to][0] - map[from][0];
            y = map[to][1] - map[from][1];
            
            temp = solve(cur_N + 2, del_x + x, del_y + y);
            if (temp < local_min)
                local_min = temp;

            temp = solve(cur_N + 2, del_x - x, del_y - y);
            if (temp < local_min)
                local_min = temp;
            
            visit[to] = 0;
        }
    }
	visit[from] = 0;
    return local_min;
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
            visit[i] = 0;

        printf("#%d %lld\n", test_case, solve(0, 0, 0));
	}
	return 0;
}