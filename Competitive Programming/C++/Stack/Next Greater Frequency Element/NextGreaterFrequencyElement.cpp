#include <iostream>
#include <stack>
#include <map>
using namespace std;

int *findNextGreaterFrequencyElement(int *elements, int n);

int main()
{
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;
    int *elements = new int[n];
    cout << "Enter the elements: ";
    for (int counter = 0; counter < n; counter++)
        cin >> elements[counter];
    int *ngf = findNextGreaterFrequencyElement(elements, n);
    cout << "Next Greater Frequency Element: ";
    for (int counter = 0; counter < n; counter++)
        cout << ngf[counter] << " ";
    delete[] elements;
}

int *findNextGreaterFrequencyElement(int *elements, int n)
{
    int *ngf = new int[n];
    stack<int> stack;
    map<int, int> freq;
    for (int counter = 0; counter < n; counter++)
        freq[elements[counter]] += 1;
    stack.push(n - 1);
    ngf[n - 1] = -1;
    for (int counter = n - 2; counter >= 0; counter--)
    {
        while (!stack.empty() && freq[elements[stack.top()]] <= freq[elements[counter]])
            stack.pop();
        if (stack.empty())
            ngf[counter] = -1;
        else
            ngf[counter] = elements[stack.top()];
        stack.push(counter);
    }
    return ngf;
}