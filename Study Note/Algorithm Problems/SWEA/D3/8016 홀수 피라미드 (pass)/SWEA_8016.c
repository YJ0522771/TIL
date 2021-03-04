#include <stdio.h>
int main(void)
{
	int test_case;
	int T;
    unsigned long int N;

	scanf("%d", &T);
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%lu", &N);
		printf("#%d %lu %lu\n", test_case, 2 * (N - 1) * (N - 1) + 1, 2 * N * N - 1);
	}
	return 0;
}