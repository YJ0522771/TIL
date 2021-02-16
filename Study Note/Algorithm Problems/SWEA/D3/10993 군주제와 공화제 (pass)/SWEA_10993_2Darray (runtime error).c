#include <stdio.h>
int main(void)
{
	int test_case;
	int T;
    int N, i, j, max_count, max_f, t, max_i;
    double temp;

	scanf("%d", &T);
    
	for (test_case = 1; test_case <= T; ++test_case)
	{
        scanf("%d", &N);
        
        int x[N], y[N], s[N];
        int p[N];
        double f[N][N];
        
        for (i = 0; i < N; i++)
        {
            scanf("%d %d %d", &x[i], &y[i], &s[i]);
            p[i] = -1;
        }
        
        for (i = 0; i < N; i++)
            for (j = 0; j < N; j++)
                f[i][j] = -1;
        
        for (i = 0; i < N; i++)
        {
            for (j = 0; j < N; j++)
            {
                if (i == j) continue;
                temp = ((x[i] - x[j]) * (x[i] - x[j])) + ((y[i] - y[j]) * (y[i] - y[j]));
                temp = s[j] / temp;		// j가 i에 행사하는 영향력
                if (s[i] < temp) f[j][i] = temp;
            }
        }
        for (i = 0; i < N; i++)
        {
            max_count = 0;
            max_f = -1;
            max_i = -1;
            for (j = 0; j < N; j++)
                if (f[j][i] > max_f)
                {
                    max_f = f[j][i];
                    max_i = j;
                    max_count++;
                }
            if (max_count > 1) { p[i] = -2; }
            else { p[i] = max_i; }
        }
        for (i = 0; i < N; i++)
        {
            t = p[i];
            while (t >= 0)
            {
                p[i] = t;
                t = p[t];
            }
        }
        
        printf("#%d", test_case);
        for (i = 0; i < N; i++)
        {
            if (p[i] >= 0) printf(" %d", p[i] + 1);
            else if (p[i] == -1) printf(" K");
            else if (p[i] == -2) printf(" D"); 
        }
        printf("\n");

	}
	return 0;
}