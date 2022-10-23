#include <iostream>
#include <stack>
#include <map>
using namespace std;

int findNextGreaterElementCount(int *elements, int n, int index);

int main()
{
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;
    int *elements = new int[n];
    cout << "Enter the elements: ";
    for (int counter = 0; counter < n; counter++)
        cin >> elements[counter];
    int queries;
    cout << "Enter the number of queries: ";
    cin >> queries;
    int *index = new int[queries];
    for (int counter = 0; counter < queries; counter++)
    {
        cout << "Enter the index: ";
        cin >> index[counter];
    }
    for (int counter = 0; counter < queries; counter++)
    {
        cout << "The number of NGEs to the right of " << index[counter] << " is " << findNextGreaterElementCount(elements, n, elements[index[counter]]) << endl;
    }
    delete[] index;
    delete[] elements;
}

int findNextGreaterElementCount(int *elements, int n, int index)
{
    map<int, int> nge;
    stack<int> stack;
    stack.push(n - 1);
    nge[elements[n - 1]] = -1;
    for (int counter = n - 2; counter >= 0; counter--)
    {
        while (!stack.empty() && elements[counter] >= elements[stack.top()])
            stack.pop();
        if (stack.empty())
            nge[elements[counter]] = -1;
        else
            nge[elements[counter]] = elements[stack.top()];
        stack.push(counter);
    }
    int count = 0;
    while (nge[index] != -1)
    {
        index = nge[index];
        count += 1;
    }
    return count;
}