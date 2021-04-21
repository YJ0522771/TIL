#include <stdio.h>

unsigned long long hs, hb;
char B[500003];
char S[100003];
int x = 257;

unsigned long long power(int a, int b)
{
    unsigned long long t, res;
    t = a;
    res = 1;
    while (b > 0)
    {
        if (b % 2)
        {
            res *= t;
            b --;
        }
        t *= t;
        b /= 2;
    }
    return res;
}

int main(void)
{
    int test_case;
    int T, ls, lb, i, j, res;

    scanf("%d", &T);

    for (test_case = 1; test_case <= T; ++test_case)
    {
        scanf("%s", B);
        scanf("%s", S);
        ls = 0;
        while (S[ls] != '\0')
            ls++;
        lb = 0;
        while (B[lb] != '\0')
            lb++;
        // printf("%d %d\n", ls, lb);

        hs = 0;
        for (i = 0; i < ls; i++)
            hs += S[i] * power(x, ls - i - 1);
        // printf("%llu\n", hs);
        hb = 0;
        for (i = 0; i < ls; i++)
            hb += B[i] * power(x, ls - i - 1);
        // printf("%llu\n", hb);

        res = 0;
        if (hs == hb)
            res++;
        for (i = 1; i < lb - ls + 1; i++)
        {
            hb *= x;
            hb -= B[i - 1] * power(x, ls);
            hb += B[i + ls - 1];
            if (hb == hs)
                res++;
        }
        printf("#%d %d\n", test_case, res);
    }
    return 0;
}