#include<iostream>
using namespace std;
int main()
{
    int arr[100][100],n,m;
    cout<<"Enter Row and Column:"<<endl;
    cin>>n>>m;
    cout<<endl;
 for(int i=0;i<n;i++)
   {
       for(int j=0;j<m;j++)
       {
          cin>>arr[i][j];
       }
   }
   for(int i=0;i<n;i++)
   {
       for(int j=0;j<m;j++)
       {
          cout<<arr[i][j]<<"  ";
       }
       cout<<endl;
   }
    for(int i=0;i<n;i++)
   {
       for(int j=0;j<m;j++)
       {
           if(i==0 || i==n-1)
           {
               cout<<arr[i][j]<<" ";
           }
           else if(i+j==n-1)
           {
               cout<<arr[i][j]<<" ";
           }
       }
   }
return 0;
}
