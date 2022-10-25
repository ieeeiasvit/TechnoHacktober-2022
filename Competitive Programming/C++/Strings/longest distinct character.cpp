#include<bits/stdc++.h>
#include<string.h>
#include<algorithm>
using namespace std;
int para(string s){
   int m=s.size();
   int k=1;
   vector<int>v;
   v.push_back(s[0]);
   for(int i=1;i<m;i++){
     if((find(v.begin(), v.end(), s[i]) == v.end())){
        v.push_back(s[i]);
        int p=v.size();
        k=max(k,p);
     }else if(find(v.begin(), v.end(), s[i]) != v.end()){
        v.clear();
        v.push_back(s[i]);
        int j=i-1;
        while(s[j]!=s[i]){
            v.push_back(s[j]);
            j--;
        }
        }
     }
   
   return k;
}

int main(){
   string s="aewergrththy";
    cout<<para(s);
}