#include <stdio.h>
int main(void)
{
	int test_case;
	int T, count;
    long int A, B;
	
	scanf("%d", &T);
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%ld %ld", &A, &B);
        count = 1;
        while (B > A)
        {
            if (B % 10 == 1)
                B /= 10;
            else if (B % 2)
                break;
            else
                B /= 2;
            count++;
        }
        printf("#%d ", test_case);
        if (B == A)
            printf("%d\n", count);
        else
            printf("-1\n");
	}
	return 0;
}