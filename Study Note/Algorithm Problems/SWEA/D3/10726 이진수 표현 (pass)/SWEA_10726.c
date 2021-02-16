#include <stdio.h>
int main(void)
{
	int test_case;
	int T, N, M, i;
    int result;

	scanf("%d", &T);
	for (test_case = 1; test_case <= T; ++test_case)
	{
        scanf("%d %d", &N, &M);
        result = 0;
        for (i = 0; i < N; i++)
        {
            if (M % 2 == 0) break;
            if (i == N - 1) result = 1;
            M = M>>1;
        }
        if (result == 1) printf("#%d ON\n", test_case);
        else printf("#%d OFF\n", test_case);
	}
	return 0;
}