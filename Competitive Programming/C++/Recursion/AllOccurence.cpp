#include <bits/stdc++.h>
using namespace std;

int allOcc(int *arr, int i, int *out, int j, int n, int key)
{
    if (n == i)
        return j;
    if (arr[i] == key)
    {
        out[j] = i;
        return allOcc(arr, i + 1, out, j + 1, n, key);
    }
    return allOcc(arr, i + 1, out, j, n, key);
}

int main()
{
    int arr[] = {4, 56, 8, 8, 7, 8, 6};
    int n = sizeof(arr) / sizeof(int);
    int out[] = {};
    int j = allOcc(arr, 0, out, 0, n, 8);
    for (int i = 0; i < j; i++)
    {
        cout << out[i] << " ";
    }

    return 0;
}