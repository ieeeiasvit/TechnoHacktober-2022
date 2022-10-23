#include <iostream>
using namespace std;

char *stack;
int top = 0;
string toPrefix(string);
int getPrecedence(char);

int main()
{
    string infix;
    cout << "Enter the infix expression: ";
    cin >> infix;
    string prefix = toPrefix(infix);
    cout << "Prefix expression: " << prefix;
}

string toPrefix(string infix)
{
    string postfix;
    stack = new char[infix.length()];
    for (int counter = infix.length() - 1; counter >= 0; counter--)
    {
        if (infix[counter] == ')')
        {
            stack[++top] = infix[counter];
        }
        else if (infix[counter] == '(')
        {
            while (stack[top] != ')')
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
        {
            postfix += infix[counter];
        }
    }
    while (top > 0)
    {
        postfix += stack[top];
        top--;
    }
    string prefix;
    for (int counter = postfix.length() - 1; counter >= 0; counter--)
    {
        prefix += postfix[counter];
    }
    delete[] stack;
    return prefix;
}

int getPrecedence(char element)
{
    if (element == '^')
        return 3;
    else if (element == '*' || element == '/')
        return 2;
    else if (element == '+' || element == '-')
        return 1;
    else
        return 0;
}