#include <stdio.h>
unsigned long long keys[200003];
unsigned long long temp[200003];
char B[200003];
int x = 257;
int L;

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

// O(nlong) 정렬
void merge_sort(int left, int right)
{
    int mid, l, r, i;
    if (left >= right)
        return;
    mid = (left + right) / 2;
    merge_sort(left, mid);
    merge_sort(mid + 1, right);

    l = left;
    r = mid + 1;
    i = 0;
    while (l <= mid && r <= right)
    {
        if (keys[l] <= keys[r])
            temp[i++] = keys[l++];
        else
            temp[i++] = keys[r++];
    }
    while (l <= mid)
        temp[i++] = keys[l++];
    while (r <= right)
        temp[i++] = keys[r++];

    for (i = 0; i <= right - left; i++)
        keys[left + i] = temp[i];
    return;
}

// parametric search를 위한 참 거짓 판별
int decision(int n)
{
    unsigned long long k = 0;
    int i;
    for (i = 0; i < n; i++)
        k += B[i] * power(x, n - i - 1);
    keys[0] = k;
    for (i = 1; i < L - n + 1; i++)
    {
        k *= x;
        k -= B[i - 1] * power(x, n);
        k += B[i + n - 1];
        keys[i] = k;
    }

    // 중복되는 key값을 찾기 쉽게 하기 위해 정렬
    merge_sort(0, L - n);

    //for (i = 0; i < L - n + 1; i++)
        //printf("%llu ", keys[i]);
    //printf("\n");
    for (i = 0; i < L - n; i++)
        if (keys[i] == keys[i + 1])
            return 1;
    return 0;
}

int main(void)
{
    int test_case;
    int T, left, right, mid, res;

    scanf("%d", &T);
    for (test_case = 1; test_case <= T; ++test_case)
    {
        scanf("%d", &L);
        scanf("%s", B);

        // 이진 탐색
        left = 1;
        right = L;
        while (left <= right)
        {
            mid = (left + right) / 2;
            res = decision(mid);
            if (res)
                left = mid + 1;
            else
                right = mid - 1;
            //printf("%d %d\n", mid, res);
        }
        if (res)
            res = mid;
        else
            res = mid - 1;
        printf("#%d %d\n", test_case, res);
    }
    return 0;
}