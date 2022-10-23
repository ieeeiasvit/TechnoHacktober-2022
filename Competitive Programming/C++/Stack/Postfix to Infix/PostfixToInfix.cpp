#include <iostream>
using namespace std;

string *stack;
int top = -1;
string toInfix(string);

int main()
{
    string postfix;
    cout << "Enter the postfix expression: ";
    cin >> postfix;
    string infix = toInfix(postfix);
    cout << "Prefix expression: " << infix;
}

string toInfix(string postfix)
{
    string infix;
    stack = new string[postfix.length()];
    for (int counter = 0; counter < postfix.length(); counter++)
    {
        char character = postfix[counter];
        if (character == '^' || character == '*' || character == '/' || character == '+' || character == '-')
        {
            string operand2 = stack[top];
            top--;
            string operand1 = stack[top];
            top--;
            stack[++top] = '(' + operand1 + character + operand2 + ')';
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