#include <stdio.h>
int main(void)
{
    int test_case;
    int T, i, state;
    int count[26];
    char s[5];

    scanf("%d", &T);
    for (test_case = 1; test_case <= T; ++test_case)
    {
        scanf("%s", s);
        for (i = 0; i < 26; i++)
            count[i] = 0;
        for (i = 0; i < 5; i++)
            count[s[i] - 'A']++;

        state = 0;
        for (i = 0; i < 26; i++)
            if (count[i] == 2)
                state++;
        if (state == 2)
            printf("#%d Yes\n", test_case); 
        else
            printf("#%d No\n", test_case); 
    }
    return 0;
}