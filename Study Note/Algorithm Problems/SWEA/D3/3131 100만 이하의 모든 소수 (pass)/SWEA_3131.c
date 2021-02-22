#include <stdio.h>
int main(void)
{
    int N = 1000001;
	int i, j;
	char p_test[N];
    for (i = 0; i < N; i++)
        p_test[i] = 1;
    
    for (i = 2; i < N; i++)
    {
        if (p_test[i] == 1)
        {
            printf("%d ", i);
        	for (j = 2 * i; j < N; j += i)
              p_test[j] = 0;
        }
    }
	printf("\n");
	return 0;
}