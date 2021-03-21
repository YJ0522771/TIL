#include <stdio.h>
int main(void)
{
	int test_case;
	int T, N, i, up, down, cur, last;
	
	scanf("%d", &T);
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
        scanf("%d", &N);
        up = 0;
        down = 0;
        scanf("%d", &last);
		for (i = 1; i < N; i++)
        {
            scanf("%d", &cur);
            if (last < cur && up < cur - last)
                up = cur - last;
            else if (last > cur && down < last - cur)
                down = last - cur;
            last = cur;
        }
        printf("#%d %d %d\n", test_case, up, down);
	}
	return 0;
}