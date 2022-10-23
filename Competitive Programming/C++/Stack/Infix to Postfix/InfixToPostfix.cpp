#include <iostream>
using namespace std;

char *stack;
int top = 0;
string infix;
string toPostfix(string);
int getPrecedence(char character);

int main()
{
    cout << "Enter the infix expression: ";
    cin >> infix;
    string postfix = toPostfix(infix);
    cout << "Postfix expression: " << postfix;
}

string toPostfix(string infix)
{
    stack = new char[infix.length()];
    string postfix;
    for (int counter = 0; counter < infix.length(); counter++)
    {
        if (infix[counter] == '(')
            stack[++top] = infix[counter];
        else if (infix[counter] == ')')
        {
            while (stack[top] != '(')
            {
                postfix += stack[top];
                top--;
            }
            top--;
        }
        else if (getPrecedence(infix[counter]))
        {
            while (top >= 0)
            {
                if (getPrecedence(stack[top]) < getPrecedence(infix[counter]))
                {
                    stack[++top] = infix[counter];
                    break;
                }
                else if (getPrecedence(stack[top]) >= getPrecedence(infix[counter]))
                {
                    postfix += stack[top];
                    top--;
                }
            }
        }
        else
            postfix += infix[counter];
    }
    while (top >= 0)
    {
        postfix += stack[top];
        top--;
    }
    delete[] stack;
    return postfix;
}

int getPrecedence(char character)
{
    if (character == '^')
        return 3;
    else if (character == '/' || character == '*')
        return 2;
    else if (character == '+' || character == '-')
        return 1;
    else
        return 0;
}