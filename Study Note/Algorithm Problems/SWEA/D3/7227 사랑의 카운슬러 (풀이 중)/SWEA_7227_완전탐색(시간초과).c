#include <stdio.h>
int map[21][2];
int match[21][21][2];
int visit[21];

unsigned long int solve(int N, int cur_N, int del_x, int del_y)
{
    int i,j, from, to, x, y;
    unsigned long int temp, local_min;
    local_min = 80000000000;
    
    if (N == cur_N)
    {
        temp = (unsigned long int)del_x * del_x;
        temp += (unsigned long int)del_y * del_y;
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
            x = match[from][to][0];
            y = match[from][to][1];
            temp = solve(N, cur_N + 2, del_x + x, del_y + y);
            if (temp < local_min)
                local_min = temp;
            
            x = match[to][from][0];
            y = match[to][from][1];
            temp = solve(N, cur_N + 2, del_x + x, del_y + y);
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
	int T, N, i, j;

	scanf("%d", &T);

	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d", &N);
        for (i = 1; i <= N; i++)
            scanf("%d %d", &map[i][0], &map[i][1]);
        
        for (i = 1; i <= N; i++) 
            for (j = 1; j <= N; j++)
            {
                match[i][j][0] = map[i][0] -  map[j][0];
                match[i][j][1] = map[i][1] -  map[j][1];
            }
        
        for (i = 1; i <= N; i++)
            visit[i] = 0;

        printf("#%d %lu\n", test_case, solve(N, 0, 0, 0));
	}
	return 0;
}