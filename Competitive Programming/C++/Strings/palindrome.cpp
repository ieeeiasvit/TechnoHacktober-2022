#include<bits/stdc++.h>
using namespace std;

int para(string s){
    int n=s.length();
    int i=0;int j=n-1;
    if(n%2==0){
    while(i<j){
        if(s[i]==s[j]){
            i++;j--;
        }else{
            break;
        }
    }
    }else{
        while(i<j){
            if(s[i]==s[j]){
            i++;j--;
        }else{
            break;
        }
        }
    }
    
   if(i==j+1 || i==j){
    return 1;
   }else{
    return 0;
   }
}

int main(){
    string s="pjxcxjp";
    cout<<para(s);
}