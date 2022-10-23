#include <iostream>
#include <stack>
using namespace std;

int *findNextGreaterElement(int *elements, int n);

int main()
{
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;
    int *elements = new int[n];
    cout << "Enter the elements: ";
    for (int counter = 0; counter < n; counter++)
        cin >> elements[counter];
    int *nge = findNextGreaterElement(elements, n);
    cout << "Next Greater Elements: ";
    for (int counter = 0; counter < n; counter++)
        cout << nge[counter] << " ";
    delete[] elements;
}

int *findNextGreaterElement(int *elements, int n)
{
    int *nge = new int[n];
    stack<int> stack;
    stack.push(n - 1);
    nge[n - 1] = -1;
    for (int counter = n - 2; counter >= 0; counter--)
    {
        while (!stack.empty() && elements[counter] >= elements[stack.top()])
            stack.pop();
        if (stack.empty())
            nge[counter] = -1;
        else
            nge[counter] = elements[stack.top()];
        stack.push(counter);
    }
    return nge;
}