#include <stdio.h>
int main(void)
{
	int test_case;
	int T, N, M;

	scanf("%d", &T);
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d %d", &N, &M);
		printf("#%d %d %d\n",test_case, M - (N - M), N - M);
	}
	return 0;
}