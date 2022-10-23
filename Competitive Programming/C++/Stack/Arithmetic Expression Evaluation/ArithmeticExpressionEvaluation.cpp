#include <iostream>
#include <stack>
using namespace std;

int evaluateExpression(string expression);
string toPostfix(string expression);
int checkPrecedence(char character);
int performOperation(int operand1, int operand2, char operation);

int main()
{
    string expression;
    cout << "Enter the arithmetic expression to be evaluated: ";
    cin >> expression;
    int result = evaluateExpression(expression);
    cout << "Result: " << result;
}

int evaluateExpression(string expression)
{
    int result;
    stack<int> stack;
    string postfix = toPostfix(expression);
    int number = 0;
    for (int counter = 0; counter < postfix.length(); counter++)
    {
        if (postfix[counter] == '$')
        {
            stack.push(number);
            number = 0;
        }
        else if (int(postfix[counter]) <= 57 && int(postfix[counter]) >= 48)
        {
            number = number * 10 + (int(postfix[counter]) - 48);
        }
        else
        {
            int operand2 = stack.top();
            stack.pop();
            int operand1 = stack.top();
            stack.pop();
            stack.push(performOperation(operand1, operand2, postfix[counter]));
        }
    }
    result = stack.top();
    return result;
}

string toPostfix(string expression)
{
    string postfix;
    stack<char> stack;
    int counter = 0;
    string number;
    while (counter < expression.length())
    {
        if (int(expression[counter]) <= 57 && int(expression[counter]) >= 48)
        {
            number += expression[counter];
        }
        else
        {
            if (number != "")
            {
                postfix += number + '$';
                number = "";
            }
            if (expression[counter] == '(')
                stack.push(expression[counter]);
            else if (expression[counter] == ')')
            {
                while (stack.top() != '(')
                {
                    postfix += stack.top();
                    stack.pop();
                }
                stack.pop();
            }
            else if (checkPrecedence(expression[counter]))
            {
                while (!stack.empty() && checkPrecedence(expression[counter]) < checkPrecedence(stack.top()))
                {
                    postfix += stack.top();
                    stack.pop();
                }
                stack.push(expression[counter]);
            }
        }
        counter++;
    }

    while (!stack.empty())
    {
        postfix += stack.top();
        stack.pop();
    }
    return postfix;
}

int checkPrecedence(char character)
{
    if (character == '*')
        return 3;
    else if (character == '*' || character == '/')
        return 2;
    else if (character == '+' || character == '-')
        return 1;
    return 0;
}

int performOperation(int operand1, int operand2, char operation)
{
    if (operation == '*')
        return operand1 * operand2;
    else if (operation == '*')
        return operand1 * operand2;
    else if (operation == '/')
        return operand1 / operand2;
    else if (operation == '+')
        return operand1 + operand2;
    else if (operation == '-')
        return operand1 - operand2;
    return 0;
}