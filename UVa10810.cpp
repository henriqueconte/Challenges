#include<cstdio>
using namespace std;

long long int invertCounter = 0;
int numberList[500000];

void getTogether(int low,int mid,int high,int arr[])
{
    int lowCounter = low, highCounter = mid + 1, bufferCounter = 0;

    while(lowCounter <= mid && highCounter <= high){
        if(arr[highCounter] < arr[lowCounter]){

            numberList[bufferCounter++] = arr[highCounter++];
            invertCounter = invertCounter + (mid - lowCounter + 1);
        }

        else numberList[bufferCounter++] = arr [lowCounter++];
    }
    while(lowCounter <= mid){
         numberList[bufferCounter++] = arr[lowCounter++];
    }

    while(highCounter <= high) {
        numberList[bufferCounter++] = arr[highCounter++];
    }
    for(bufferCounter = 0; low <= high; low++){
        arr[low] = numberList[bufferCounter++];
    }

}


void mergesort(int low,int high,int arr[])

{
    if(low==high)
        return;

    int mid=(low + high)/2;

    mergesort(low, mid, arr);
    mergesort(mid+1, high, arr);
    getTogether(low, mid, high, arr);
}





int main()
{
    int loopCount;
    while(scanf("%d",&loopCount)){
        if(loopCount == 0)
            return 0;

        int arr[500000];
        invertCounter = 0;

        for(int i = 0; i < loopCount; i++){
            scanf("%d",&arr[i]);
        }

        mergesort(0,loopCount-1,arr);
        printf("%lld\n",invertCounter);
    }
}


/*
Hi,

This is an automated response from UVa Online Judge.

Your submission with number 23199280 for the problem 10810 - Ultra-QuickSort has received the verdict Accepted.

Congratulations! Now it is time to try a new problem.

Best regards,

The UVa Online Judge team
*/
