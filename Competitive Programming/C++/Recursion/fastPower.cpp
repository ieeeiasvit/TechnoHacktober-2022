#include <bits/stdc++.h>
using namespace std;

int power(int base, int pow)
{
    if (pow == 0)
        return 1;

    int ans = power(base, pow / 2);

    if (pow & 1)
        return base * ans * ans;
    else
        return ans * ans;
}

int main()
{
    int pow;
    int base;
    cin>>base>>pow;
    cout << power(base,pow) << endl;
    return 0;
}