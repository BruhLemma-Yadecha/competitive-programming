#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    scanf("%d", &n);
    int pile[n];
    int top = -1;
    int next_tyre = 1;
    int shufflings = 0;
    for (int i = 0; i < 2 * n; ++i)
    {
        char command;
        scanf(" %c", &command);
        if (command == 'a')
        {
            int tyre;
            scanf("%d", &tyre);
            pile[++top] = tyre;
        }
        else
        {
            if (top >= 0)
            {
                if (next_tyre != pile[top])
                {
                    shufflings += 1;
                    top = -1;
                }
                else
                {
                    --top;
                }
            }
            ++next_tyre;
        }
    }
    printf("%d\n", shufflings);
    return 0;
}