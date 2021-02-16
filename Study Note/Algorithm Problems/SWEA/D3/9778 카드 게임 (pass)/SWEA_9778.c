#include <stdio.h>
int main(void)
{
	int test_case;
	int T, N, i, sum, t1, t2;

	scanf("%d", &T);

	for (test_case = 1; test_case <= T; ++test_case)
	{
        int card[12] = {0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 16, 4};
		scanf("%d", &N);
        sum = 0;
		for (i = 0; i < N; i++)
        {
            scanf("%d", &t1);
            sum += t1;
            card[t1]--;
        }
        sum = 21 - sum;
        t1 = 0;
        t2 = 0;
        for (i = 2; i < 12; i++)
        {
            if (i <= sum) t1 += card[i];
            else t2+= card[i];
        }
        if (t1 <= t2) printf("#%d STOP\n", test_case);
        else printf("#%d GAZUA\n", test_case);
	}
	return 0;
}