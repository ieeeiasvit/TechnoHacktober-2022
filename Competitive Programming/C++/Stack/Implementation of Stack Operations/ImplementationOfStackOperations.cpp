#include <iostream>
using namespace std;

int n;
int *stack;
int top = -1;
void push(int element);
void pop();
void display();
int maximum();
int minimum();
void search(int element);

int main()
{
    cout << "Enter the size of the stack: ";
    cin >> n;
    stack = new int[n];
    while (true)
    {
        cout << "\n**********************Menu:**********************" << endl;
        cout << "1. Push\n2. Pop\n3. Display Stack\n4. Maximum element\n5. Minimum element\n6. Search\n7. Exit\nChoice: ";
        int choice;
        cin >> choice;
        switch (choice)
        {
        case 1:
        {
            cout << "Enter the element to be pushed: ";
            int element;
            cin >> element;
            push(element);
            break;
        }
        case 2:
        {
            pop();
            break;
        }
        case 3:
        {
            display();
            break;
        }
        case 4:
        {
            if (top < 0)
                cout << "There are no elements in the stack";
            else
            {
                int max = maximum();
                cout << "The maximum element in the stack is " << max;
            }
            break;
        }
        case 5:
        {
            if (top < 0)
                cout << "There are no elements in the stack";
            else
            {
                int min = minimum();
                cout << "The minimum element in the stack is " << min;
            }
            break;
        }
        case 6:
        {
            int element;
            cout << "Enter the element to be searched in the stack: ";
            cin >> element;
            search(element);
            break;
        }
        case 7:
        {
            exit(0);
            break;
        }
        default:
        {
            cout << "Invalid Input. Please try again";
        }
        }
    }
    delete[] stack;
}

void push(int element)
{
    if (top >= n - 1)
        cout << "Error: Stack is full. Cannot insert " << element;
    else
    {
        stack[++top] = element;
        cout << element << " pushed into the stack";
    }
}

void pop()
{
    if (top < 0)
    {
        cout << "Error: Stack is empty. Cannot pop anymore";
    }
    else
    {
        top--;
        cout << "Popped element = " << stack[top + 1];
    }
}

void display()
{
    cout << "Stack: ";
    for (int counter = 0; counter <= top; counter++)
    {
        cout << stack[counter] << " ";
    }
}

int maximum()
{
    int max = stack[top];
    for (int counter = 0; counter <= top; counter++)
        if (max < stack[counter])
            max = stack[counter];
    return max;
}

int minimum()
{
    int min = stack[top];
    for (int counter = 0; counter <= top; counter++)
        if (min > stack[counter])
            min = stack[counter];
    return min;
}

void search(int element)
{
    bool flag = false;
    for (int counter = 0; counter <= top; counter++)
    {
        if (element == stack[counter])
        {
            flag = true;
            break;
        }
    }
    if (flag)
        cout << element << " is present in the stack";
    else
        cout << element << " is not present in the stack";
}