#include <stdio.h>
int a[9];
int b[9];
int visit[9];
int win, lose;

void solve(int cur, int a_sum, int b_sum)
{
    int i;
    if (cur == 9)
    {
        if (a_sum > b_sum)
            win++;
        else if (b_sum > a_sum)
            lose++;
        return;
    }
    for (i = 0; i < 9; i++)
    {
        if (!visit[i])
        {
            visit[i] = 1;
            if (a[cur] > b[i])
                solve(cur + 1, a_sum + a[cur] + b[i], b_sum);
            else
                solve(cur + 1, a_sum, b_sum + a[cur] + b[i]);
            visit[i] = 0;
        }
    }
    return;
}

int main(void)
{
	int test_case;
	int T, i, j;
    int count[19];
    
	scanf("%d", &T);
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
		for (i = 1; i <= 18; i++)
            count[i] = 1;
        for (i = 0; i < 9; i++)
        {
            scanf("%d", &a[i]);
            count[a[i]] = 0;
        }
        j = 0;
        for (i = 1; i <= 18; i++)
			if (count[i])
            {
                b[j] = i;
                j++;
            }
        
        win = 0;
        lose = 0;
        for (i = 0; i < 9; i++)
            visit[i] = 0;
        solve(0, 0, 0);
        
        printf("#%d %d %d\n", test_case, win, lose);
        
	}
	return 0;
}