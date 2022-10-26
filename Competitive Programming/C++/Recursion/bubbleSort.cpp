#include <bits/stdc++.h>
using namespace std;

void bubbleSort(int *arr, int n)
{
    if (n == 0)
        return;

    for (int i = 0; i < n - 1; i++)
    {
        if (arr[i] > arr[i + 1])
        {
            swap(arr[i], arr[i + 1]);
        }
    }

    bubbleSort(arr, n - 1);
}
void bubbleSort2(int *arr, int n, int j)
{

    if (n == 1)
    {
        return;
    };

    if (j == n - 1)
    {
        return bubbleSort2(arr, n - 1, 0);
    }

    if (arr[j] > arr[j + 1])
    {
        swap(arr[j], arr[j + 1]);
    }

    bubbleSort2(arr, n, j + 1);
}

int main()
{
    int arr[] = {9, 5, 4, 3, 2, 1, 1, 5};
    int n = sizeof(arr) / sizeof(int);

    bubbleSort2(arr, n, 0);
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << endl;
    }

    return 0;
}