#include <stdio.h>
int main(void)
{
	int test_case;
	int T, N, D, count, temp, res, i;

	scanf("%d", &T);

	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d %d", &N, &D);
		count = 0;
        res = 0;
        for (i = 0; i < N; i++)
        {
            scanf("%d", &temp);
            if (temp)
            {
                if (count >= D)
                    res += (count / D);
                count = 0;
            }
            else
                count++;
        }
        if (count >= D)
            res += (count / D);
        printf("#%d %d\n", test_case, res);
	}
	return 0;
}