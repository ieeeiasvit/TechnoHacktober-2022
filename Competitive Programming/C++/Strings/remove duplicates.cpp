#include <bits/stdc++.h>
using namespace std;

string dup(string s){
    string ans;
    int n=s.size();
    unordered_map<char,int>m;
    for(int i=0;i<n;i++){
        m[s[i]]++;
    }

    for(int i=0;i<n;i++){
        if(m.find(s[i])!=m.end() && m[s[i]]!=0){
            ans+=s[i];
            m[s[i]]=0;
        }
    }
    return ans;
}

int main(){
  string s="gfg";
  cout<<dup(s);    
}
