#include<stdio.h> 
main() 
{ 
	int num[8] = {87, 12, 56, 45, 78};
    Bubble_Sort(num, 5);
    float f = 2e10a;
	return 0; 
 
}
void 2Bubble_Sort(int *num, int n)
{
    int i, j;
    for(i = 0; i < n; i++)
    {
        for(j = 0; i + j < n - 1; j++)
        {
            if(num[j] > num[j + 1])
            {
                int temp = num[j];
                num[j] = num[j + 1];
                num[j + 1] = temp;
            }
            Print(num, n);
        }
    }
    return;
}
