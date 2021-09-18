#include<stdio.h>
int getmissing(int a[],int n)
{
    int a,total;
    total=(n+1)+(n+2)/2;
    for(i=0; i<n;i++)
    total=total-a[i];
    printf("%d",total);

}
int main()
{
   int a[]=[1,2,4,5,6];
   miss= getmissing(a[],5);
   printf("%d",miss);

}
int main()
{
    int a[], i,n,small,large;
    printf("enter the element",n);
    for(i=0;i < n;i++);
    scanf("%d",i);
    small=large>a[0];
    print("small");
    for(i=1;i<n;i++);
    if a[1]>small;
    print("large")
    return 0;



}
def getpairscount(arr,n,sum):
Count=0
for i in range(0,n):
    for j in range(i+1,n):
        if arr[i]+arr[j]=sum:
            count=count+1
            return count
arr=[1,2,3,5]
n=len[arr]
sum=6
print("count pairs is",get pairs count [arr,n,sum])
}
void reverseno(int arr,int start,int end)
{
temp;
while(end>start)
    temp=int start;
    int start =int end;
    int end=temp;
    start++;
    end--;
}

