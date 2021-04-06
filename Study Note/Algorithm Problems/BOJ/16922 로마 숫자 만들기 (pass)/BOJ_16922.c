#include <stdio.h>
int exist[1001];
int main(void)
{
	int N, i, j, k, temp, count;

    for (i = 0; i < 1001; i++)
        exist[i] = 0;
    scanf("%d", &N);

    temp = 0;
    count = 0;
    for (i = 0; i <= N; i++)
        for (j = 0; j <= N - i; j++)
            for (k = 0; k <= N - i - j; k++)
            {
                temp = (1 * i) + (5 * j) + (10 * k) + (50 * (N - i - j - k));
                if (!exist[temp])
                {
                    exist[temp] = 1;
                    count++;
                }
            }
    printf("%d\n", count);
	return 0; 
}