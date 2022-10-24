//  C++ program to reverse a string
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    // string s;
    // cin>>s;
    // string s_rev;
    // for(int i=s.size()-1;i>=0;--i){
    //     // s_rev=s_rev+s[i];
    //     s_rev.push_back(s[i]);
    // }
    // cout<<s_rev<<"\n";
    
    // if(s==s_rev){
    // 	cout<<"YES";
	// }
	// else{
	// 	cout<<"NO";
	// }
	
//	string s;
//    cin>>s;
//    
//    for(int i=0; i<s.size()/2; i++){
//        if(s[i]!=s[s.size()-i-1]){
//            cout<<"NO";
//        }
//        else{
//            cout<<"YES";
//        }
//    }
        string s;
      cin>>s;
        int start=0;
        int end=s.size()-1;
        
    while(start<=end)//1<10
    {
        swap(s[start],s[end]);
        start++;
        end--;
    }

    for (int i = 0; i < s.size(); i++)
    {
        cout<<s[i];
    }
}
