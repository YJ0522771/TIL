#include <stdio.h>
int main(void)
{
	int test_case;
	int T, N, K;
	
	scanf("%d", &T);

	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d  %d", &N, &K);
		if (N % K == 0) printf("#%d 0\n", test_case);
        else printf("#%d 1\n", test_case);
	}
	return 0; 
}