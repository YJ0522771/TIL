#include <stdio.h>
int main(void)
{
	int test_case;
	int T, d;
	
	scanf("%d", &T);
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d", &d);
        printf("#%d ", test_case);
        if (d < 100)
            printf("0\n");
        else if (d <1000)
            printf("1\n");
        else if (d < 10000)
            printf("2\n");
        else if (d < 100000)
            printf("3\n");
        else if (d < 1000000)
            printf("4\n");
        else
            printf("5\n");
	}
	return 0;
}