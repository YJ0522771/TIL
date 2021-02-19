#include <stdio.h>
int main(void)
{
	int test_case;
	int T, N, i;
	unsigned long int arr[100];
    
    for (i = 0; i < 3; i++)
        arr[i] = 1;
    for (i = 3; i < 5; i++)
        arr[i] = 2;
    for (i = 5; i < 100; i++)
        arr[i] = arr[i - 1] + arr[i - 5];

	scanf("%d", &T);

	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d", &N);
		printf("#%d %lu\n", test_case, arr[N - 1]);
	}
	return 0; 
}