#include<stdio.h>
#include<math.h>
int main()
{
    int sum=0,i,n;
    printf("Enter value of n :");
    scanf("%d",&n);
    for(i=1;i<=n;i++)
        sum = sum + i ;
    printf("The answer is %d\n",&sum);
    return 0;
}
