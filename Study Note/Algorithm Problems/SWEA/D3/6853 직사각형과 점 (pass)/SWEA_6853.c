#include <stdio.h>
int main(void)
{
	int test_case;
	int T, N, x1, x2, y1, y2, res1, res2, res3, i, x, y;
	
	scanf("%d", &T);
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
        scanf("%d", &N);
        res1 = 0;
        res2 = 0;
        res3 = 0;
        for (i = 0; i < N; i++)
        {
            scanf("%d %d", &x, &y);
            if (x > x1 && x < x2 && y > y1 && y < y2)
                res1++;
            else if ((x == x1 || x == x2) && y >= y1 && y <= y2)
                res2++;
            else if ((y == y1 || y == y2) && x >= x1 && x <= x2)
                res2++;
            else
                res3++;
        }
		printf("#%d %d %d %d\n", test_case, res1, res2, res3);
	}
	return 0;
}