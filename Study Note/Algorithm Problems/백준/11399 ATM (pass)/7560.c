#include <stdio.h>
int P[1000];
int main(void)
{
	int test_case;
	int T, N, i, j, temp, idx, res;
	
	scanf("%d", &T);
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d", &N);
        for (i = 0; i < N; i++)
            scanf("%d", &P[i]);
        for (i = 0; i < N - 1; i++)
        {
            temp = P[i];
            idx = i;
            for (j = i+1; j < N; j++)
                if (temp > P[j])
                {
                    temp = P[j];
                    idx = j;
                }
            P[idx] = P[i];
            P[i] = temp;
        }
        res = 0;
        for (i = 0; i < N; i++)
            res += (P[i] * (N - i ));
        printf("#%d %d\n", test_case, res);
	}
	return 0; 
}