#include <iostream>
#include <stack>
using namespace std;

bool checkBrackets(string);

int main()
{
    string expression;
    cout << "Enter the expression: ";
    cin >> expression;
    bool flag = checkBrackets(expression);
    if (flag)
        cout << "The expression is balanced";
    else
        cout << "The expression is not balanced";
}

bool checkBrackets(string expression)
{
    stack<char> stack;
    for (int counter = 0; counter < expression.length(); counter++)
    {
        char character = expression[counter];
        if (character == '(' || character == '{' || character == '[')
            stack.push(character);
        else if (!stack.empty() && ((character == ')' && stack.top() == '(') || (character == '}' && stack.top() == '{') || (character == ']' && stack.top() == '[')))
            stack.pop();
    }
    if (stack.empty())
        return true;
    return false;
}