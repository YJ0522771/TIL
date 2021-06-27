#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

char s[20001];
char a[10001];
char b[10001];
int main(void)
{	
	int i, t, len_a, len_b;
	scanf("%s", s);

	i = 0;
	t = 1;
	while (s[i] != '\0')
	{
		if (s[i] >= '0' && s[i] <= '9')
		{
			if (t)
				a[i] = s[i];
			else
				b[i - len_a - 1] = s[i];
		}
		else
		{
			t = 0;
			len_a = i;
		}

		i++;
	};
	len_b = i - len_a - 1;

	printf("%d %d\n", len_a, len_b);
	return 0;
}