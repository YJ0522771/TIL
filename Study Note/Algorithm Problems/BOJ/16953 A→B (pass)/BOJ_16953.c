#include <stdio.h>
int main(void)
{
	int count;
    long int A, B;

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
    if (B == A)
        printf("%d\n", count);
    else
        printf("-1\n");
        
	return 0;
}