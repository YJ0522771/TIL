#include <stdio.h>
int main(void)
{
	int test_case;
	int T, N, temp, max, state, i;
    int count[41];
    long int res;
	
	scanf("%d", &T);
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d", &N);
        for (i = 0; i < 41; i++)
            count[i] = 0;
        max = 0;
        for (i = 0; i < N; i++)
        {
            scanf("%d", &temp);
            count[temp]++;
            if (max < temp)
                max = temp;
        }
        state = 1;
        temp = 0;
        for (i = max; i >= 0; i--)
        {
            if (count[i] == 0)
                state = 0;
            else if (count[i] > 2)
                state = 0;
            else if (count[i] == 2)
                temp = 1;
            else if (temp && count[i] == 1)
                state = 0;
        }
        printf("#%d ", test_case);
        if (state)
        {
            res = 1;
            for (i = max; i >= 0; i--)
                res *= count[i];
            printf("%ld\n", count[max] == 1? res * 2 : res);
        }   
        else
        	printf("%d\n", state);
	}
	return 0;
}