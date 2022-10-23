#include <iostream>
using namespace std;

string *stack;
int top = -1;
string toInfix(string);

int main()
{
    string prefix;
    cout << "Enter the prefix expression: ";
    cin >> prefix;
    string infix = toInfix(prefix);
    cout << "Infix expression: " << infix;
}

string toInfix(string prefix)
{
    string infix;
    stack = new string[prefix.length()];
    for (int counter = prefix.length() - 1; counter >= 0; counter--)
    {
        char character = prefix[counter];
        if (character == '^' || character == '*' || character == '/' || character == '+' || character == '-')
        {
            string operand1 = stack[top];
            top--;
            string operand2 = stack[top];
            top--;
            stack[++top] = "(" + operand1 + character + operand2 + ")";
        }
        else
        {
            stack[++top] = character;
        }
    }
    infix = stack[top];
    top--;
    delete[] stack;
    return infix;
}