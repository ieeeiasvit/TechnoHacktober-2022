#include <iostream>
using namespace std;

string *stack;
int top = -1;
string toPostfix(string);

int main()
{
    string prefix;
    cout << "Enter the prefix expression: ";
    cin >> prefix;
    string postfix = toPostfix(prefix);
    cout << "Postfix expression: " << postfix;
}

string toPostfix(string prefix)
{
    string postfix;
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
            stack[++top] = operand1 + operand2 + character;
        }
        else
        {
            stack[++top] = character;
        }
    }
    postfix = stack[top];
    top--;
    delete[] stack;
    return postfix;
}