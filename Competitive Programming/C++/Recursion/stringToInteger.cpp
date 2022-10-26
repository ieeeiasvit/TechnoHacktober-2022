#include <bits/stdc++.h>
using namespace std;

int stringToInteger(char *str, int n)
{
    if (n == 0)
        return 0;

    int digits = str[n - 1] - '0';
    int small_ans = stringToInteger(str, n - 1);
    return small_ans * 10 + digits;
}

int main()
{
    char str[] = {"87383269"};
    cout << stringToInteger(str, 8) << endl;

    return 0;
}