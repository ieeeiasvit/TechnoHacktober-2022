#include <iostream>
#include <stack>
using namespace std;

int findCelebrity(int **matrix, int n);

int main()
{
    int n;
    cout << "Enter the number of people in the party: ";
    cin >> n;
    int **matrix = new int *[n];
    for (int counter = 0; counter < n; counter++)
        matrix[counter] = new int[n];
    cout << "Enter the Acquaintance Matrix: " << endl;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> matrix[i][j];
    int id = findCelebrity(matrix, n);
    if (id == -1)
        cout << "There are no celebrities";
    else
        cout << "Celebrity: " << id;
    for (int counter = 0; counter < n; counter++)
        delete[] matrix[counter];
    delete[] matrix;
}

int findCelebrity(int **matrix, int n)
{
    stack<int> stack;
    for (int counter = 0; counter < n; counter++)
        stack.push(counter);
    while (stack.size() > 1)
    {
        int A = stack.top();
        stack.pop();
        int B = stack.top();
        stack.pop();
        if (matrix[A][B])
            stack.push(B);
        else
            stack.push(A);
    }
    int celebrity = stack.top();
    stack.pop();

    for (int counter = 0; counter < n; counter++)
    {
        if (celebrity != counter && (!matrix[counter][celebrity] || matrix[celebrity][counter]))
            return -1;
    }
    return celebrity;
}