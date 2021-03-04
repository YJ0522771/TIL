#include <stdio.h>
int arr[1024];

int main(void)
{
	int test_case;
	int T, K, i, j, mid;
	
	scanf("%d", &T);
	
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d", &K);
		for (i = 0; i < (1 << K) - 1; i++)
            scanf("%d", &arr[i]);
        
        printf("#%d ", test_case);
        for (i = 0; i < K; i++)
        {
            for (j = 0; j < (1 << K) - 1; j += (1 << (K - i)))
            {
                mid = (j + (j + (1 << (K - i)) - 1)) / 2;
                printf("%d ", arr[mid]);
            }
            printf("\n");
        }
	}
	return 0;
}