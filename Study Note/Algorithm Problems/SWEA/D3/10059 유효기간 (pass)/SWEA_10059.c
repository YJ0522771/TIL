#include <stdio.h>
int main(void)
{
	int test_case;
	int T, num1, num2;

	scanf("%d", &T);

	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d", &num1);
        num2 = num1 % 100;
        num1 /= 100;
        char state[2] = {'y', 'y'};
        
        if (num1 <= 12 && num1 >= 1) state[0] = 'm';
        if (num2 <= 12 && num2 >= 1) state[1] = 'm';
        
        if (state[0] == 'm' && state[1] == 'm') printf("#%d AMBIGUOUS\n", test_case);
        else if (state[0] == 'y' && state[1] == 'm') printf("#%d YYMM\n", test_case);
        else if (state[0] == 'm' && state[1] == 'y') printf("#%d MMYY\n", test_case);
        else printf("#%d NA\n", test_case);
	}
	return 0;
}