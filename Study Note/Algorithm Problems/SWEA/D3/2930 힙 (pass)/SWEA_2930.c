#include <stdio.h>
#define END 0
long int heap[100001];

void push(long int num)
{
    int child = ++heap[END];
    int parent;
    while (child > 1)
    {
        parent = child / 2;
        if (heap[parent] < num)
            heap[child] = heap[parent];
        else
            break;
        child = parent;
    }
    heap[child] = num;
    return;
}

long int pop()
{
    long int temp = heap[1];
    long int k = heap[heap[END]--];
    int parent = 1;
    int child;
    while (2 * parent <= heap[END])
    {
        if (2 * parent < heap[END] && heap[2 * parent + 1] >= heap[2 * parent])
            child = 2 * parent + 1;
        else
            child = 2 * parent;
        if (k > heap[child])
            break;
        else
            heap[parent] = heap[child];
        parent = child;
    }
    heap[parent] = k;
    return temp;
}

int main(void)
{
	int test_case;
	int T, N, oper, i, j;
    long int num;
	
	scanf("%d", &T);
	for (test_case = 1; test_case <= T; ++test_case)
	{
		scanf("%d", &N);
        heap[END] = 0;
        printf("#%d", test_case);
        for (i = 0; i < N; i++)
        {
            scanf("%d", &oper);
            if (oper == 1)
            {
                scanf("%ld", &num);
                push(num);
            }
            else
            {
                if (heap[END])
                	printf(" %ld", pop());
                else
                    printf(" -1");
            }
        }
        printf("\n");
	}
	return 0;
}