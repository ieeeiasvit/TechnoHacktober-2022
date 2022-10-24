#include <bits/stdc++.h>
using namespace std;

void merge(int *arr, int start, int end)
{
    int mid = start + (end - start) / 2;
    int temp[start + end];

    int i = start;
    int j = mid + 1;
    int k = start;

  
    while (i <= mid && j <= end)
    {
        if (arr[i] <= arr[j])
        {
            temp[k++] = arr[i++];
        }
        else if(arr[i] >arr[j])
        {
            temp[k++] = arr[j++];
        }
    }
    
    while (i <= mid)
    {
        temp[k++] = arr[i++];
    }
    while (j <= end)
    {
        temp[k++] = arr[j++];
    }
    

    for (int i = start; i <= end; i++)
    {
        arr[i] = temp[i];
    }
}

void mergeSort(int *arr, int start, int end)
{
    if (start>=end)
        {return;}
    int mid = start + (end - start) / 2;

    // left side sorting
    mergeSort(arr, start, mid);
    // right side sorting
    mergeSort(arr, mid + 1, end);
        
    // merging
    merge(arr, start, end);
}

int main()
{
    int arr[] = {4, 6, 5, 32, 1};
    int n = sizeof(arr) / sizeof(int);
    mergeSort(arr, 0, n - 1);
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << endl;
    }

    return 0;
}