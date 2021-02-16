#include <stdio.h>
int main(void)
{
	int test_case;
	int T;
    int N, i, j, t, max_i;
    double temp, max_f;
    int x[1000], y[1000], s[1000];
    int p[1000];

	scanf("%d", &T);
    
	for (test_case = 1; test_case <= T; ++test_case)
	{
        scanf("%d", &N);
        
        for (i = 0; i < N; i++)
        {
            scanf("%d %d %d", &x[i], &y[i], &s[i]);
            p[i] = -1;
        }
        
        for (i = 0; i < N; i++)
        {
            max_f = -1;
            for (j = 0; j < N; j++)
            {
                if (i == j) continue;
                temp = ((x[i] - x[j]) * (x[i] - x[j])) + ((y[i] - y[j]) * (y[i] - y[j]));
                temp = s[j] / temp;		// j가 i에 행사하는 영향력
                if ((double)s[i] < temp)
                {
                    if (max_f < temp)
                    {
                        max_f = temp;
                        p[i] = j;
                    }
                    else if (max_f == temp)
                    {
                        p[i] = -2;
                    }
                }
            }
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