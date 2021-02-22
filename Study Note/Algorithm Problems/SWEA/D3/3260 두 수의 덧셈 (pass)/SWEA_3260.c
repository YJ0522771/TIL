#include <stdio.h>
int main(void)
{
	int test_case;
	int T, i, j, N, M, c;
    char A[101], B[101];

	scanf("%d", &T);
    
	for (test_case = 1; test_case <= T; ++test_case)
	{
        char ans[102];
        scanf("%s %s", A, B);
        
        i = 0;
        while (A[i] != '\0')
        	i++;
        N = i;
        i = 0;
        while (B[i] != '\0')
        	i++;
        M = i;
        
        c = 0;
        i = 1;
        while (N - i >= 0 && M - i >= 0)
        {
            if (A[N - i] - '0' + B[M - i] - '0' + c > 9)
            {
                ans[i - 1] = A[N - i] + B[M - i] - '0' + c - 10;
                c = 1;
            }
            else
            {
                ans[i - 1] = A[N - i] + B[M - i] - '0' + c;
                c = 0;
            } 
            i++;
        }
        
        if (N - i >= 0)
        {
            while (N - i >= 0)
            {
                if (A[N - i] - '0' + c > 9)
                {
                    ans[i - 1] = A[N - i] + c - 10;
                    c = 1;
                }
                else
                {
                    ans[i - 1] = A[N - i] + c;
                    c = 0;
                }
                i++;
            }
        }
        else if (M - i >= 0)
        {
            while (M - i >= 0)
            {
                if (B[M - i] - '0' + c > 9)
                {
                    ans[i - 1] = B[M - i] + c - 10;
                    c = 1;
                }
                else
                {
                    ans[i - 1] = B[M - i] + c;
                    c = 0;
                }
                i++;
            }
        }
        if (c == 1)
        {
            ans[i - 1] = '1';
            i++;
        }
        ans[i - 1] = '\0';
        N = i - 1;
        
        printf("#%d ",  test_case);
        for (i = N - 1; i >= 0; i--)
          printf("%c", ans[i]);
        printf("\n"); 
	}
	return 0;
}