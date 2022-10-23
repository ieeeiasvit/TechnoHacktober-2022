#include <iostream>
using namespace std;

string *stack;
int top = -1;
string toPrefix(string);

int main()
{
    string postfix;
    cout << "Enter the postfix expression: ";
    cin >> postfix;
    string prefix = toPrefix(postfix);
    cout << "Prefix expression: " << prefix;
}

string toPrefix(string postfix)
{
    string prefix;
    stack = new string[postfix.length()];
    for (int counter = 0; counter < postfix.length(); counter++)
    {
        char character = postfix[counter];
        if (character == '^' || character == '*' || character == '/' || character == '+' || character == '-')
        {
            string operand1 = stack[top];
            top--;
            string operand2 = stack[top];
            top--;
            stack[++top] = character + operand2 + operand1;
        }
        else
        {
            stack[++top] = character;
        }
    }
    prefix = stack[top];
    top--;
    delete[] stack;
    return prefix;
}