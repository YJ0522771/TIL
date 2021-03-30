#include <stdio.h>
int main(void)
{
	int N, K, M, n, N2, K2;
    scanf("%d %d %d", &N, &K, &M);
    for (n = 1; n < N; n++)
    {
        N2 = N - n + 1;
        K2 = K % N2? K % N2 : N2;
        if (M == K2)
            break;
        M = K2 < M? M - K2 : M - K2 + N2;
    }
    printf("%d\n", n);
    return 0;
}