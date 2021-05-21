#include <stdio.h>
int main(void)
{
	int test_case;
	int T, N, i;
	
	scanf("%d", &T);
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d", &N);
        for (i = 1; i < 10; i++)
            if (N % i == 0 && N / i < 10)
                break;
        if (i == 10)
            printf("#%d No\n", test_case);
        else
            printf("#%d Yes\n", test_case);
	}
	return 0;
}