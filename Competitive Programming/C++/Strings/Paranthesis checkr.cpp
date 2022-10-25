#include<bits/stdc++.h>
using namespace std;

bool para(string s){
    int n=s.length();
    stack<char>a;
    int i=0;
    while(i<n){
        if(s[i]=='(' || s[i]=='{'|| s[i]=='[' ){
            a.push(s[i]);
        }else if(!a.empty()){
            if((s[i]==')' && a.top()=='(') ||(s[i]=='}' && a.top()=='{') || (s[i]==']' && a.top()=='[')){
                a.pop();
            }else{
                return 0;
            }
        }else{
            return 0;
            }
        
            i++;
            
    }
   if(a.empty()){
    return 1;
   }else{
    return 0;
   }
}

int main(){
    string s="{[()]}";
    para(s);
}