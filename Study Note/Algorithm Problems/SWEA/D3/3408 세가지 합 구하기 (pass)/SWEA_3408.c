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
        printf("#%d %lu %lu %lu\n", test_case, N * (N + 1) / 2, N * N, N * (N + 1));
    }
    return 0;
}