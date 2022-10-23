#include <iostream>
#include <stack>
using namespace std;

int *calculateSpan(int *, int);

int main()
{
    int n;
    cout << "Enter the number of days: ";
    cin >> n;
    int *price = new int[n];
    cout << "Enter the prices for each day: ";
    for (int counter = 0; counter < n; counter++)
        cin >> price[counter];
    int *span = calculateSpan(price, n);
    cout << "Span: ";
    for (int counter = 0; counter < n; counter++)
        cout << span[counter] << " ";
    delete[] price;
}

int *calculateSpan(int *price, int n)
{
    int *span = new int[n];
    stack<int> stack;
    stack.push(0);
    span[0] = 1;
    for (int counter = 1; counter < n; counter++)
    {
        while (!stack.empty() && price[stack.top()] <= price[counter])
            stack.pop();
        if (stack.empty())
            span[counter] = counter + 1;
        else
            span[counter] = counter - stack.top();
        stack.push(counter);
    }
    return span;
}