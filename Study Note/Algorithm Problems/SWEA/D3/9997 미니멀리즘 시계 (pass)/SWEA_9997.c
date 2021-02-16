#include <stdio.h>
int main(void)
{
	int test_case;
	int T, theta;

	scanf("%d", &T);

	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d", &theta);
		printf("#%d %d %d\n", test_case, theta / 30, (theta % 30) * 2);
	}
	return 0; 
}