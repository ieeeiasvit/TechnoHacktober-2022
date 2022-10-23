#include <iostream>
#include <stack>
using namespace std;

int maxLRProduct(int *elements, int n);

int main()
{
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;
    int *elements = new int[n];
    cout << "Enter the elements: ";
    for (int counter = 0; counter < n; counter++)
        cin >> elements[counter];
    int LRproduct = maxLRProduct(elements, n);
    cout << "The index with maximum LR product is " << LRproduct;
}

int maxLRProduct(int *elements, int n)
{
    // Li
    int *Li = new int[n];
    stack<int> stack;
    stack.push(0);
    Li[0] = 0;
    for (int counter = 1; counter < n; counter++)
    {
        while (!stack.empty() && elements[stack.top()] <= elements[counter])
            stack.pop();
        if (stack.empty())
            Li[counter] = 0;
        else
            Li[counter] = stack.top() + 1;
        stack.push(counter);
    }

    while (!stack.empty())
        stack.pop();

    // Ri
    int *Ri = new int[n];
    stack.push(n - 1);
    Ri[n - 1] = 0;
    for (int counter = n - 2; counter >= 0; counter--)
    {
        while (!stack.empty() && elements[stack.top()] <= elements[counter])
            stack.pop();
        if (stack.empty())
            Ri[counter] = 0;
        else
            Ri[counter] = stack.top() + 1;
        stack.push(counter);
    }

    // LR
    int max = Li[0] * Ri[0];
    for (int counter = 0; counter < n; counter++)
        if (max < (Li[counter] * Ri[counter]))
            max = Li[counter] * Ri[counter];

    return max;
}