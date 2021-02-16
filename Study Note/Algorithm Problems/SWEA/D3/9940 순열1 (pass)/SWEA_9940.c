#include <stdio.h>
int main(void)
{
	int test_case;
	int T, N, i, state;
	
	scanf("%d", &T);
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d", &N);
        int nums[N], count[N];
        for (i = 0; i < N; i ++)
        {
        	scanf("%d", &nums[i]);
            count[i] = 0;
        }
        state = 1;
        for (i = 0; i < N; i ++)
            count[nums[i] - 1]++;
        for (i = 0; i < N; i ++)
            if (count[i] == 0)
                state = 0;
        if (state == 0)
            printf("#%d No\n", test_case);
        else
            printf("#%d Yes\n", test_case);
	}
	return 0; 
}