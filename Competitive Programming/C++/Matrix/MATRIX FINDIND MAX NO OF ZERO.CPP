#include<iostream>

using namespace std;

int main()
{

   int a[5][5];
   int z,maxz=0,ind=-1,n,c;
   cin>>n;
   int i,j;
   for (i=0;i<n;i++)
   {
       for (j=0;j<n;j++)
       {
           cin>>a[i][j];

       }

   }
   for (j=0;j<n;j++)
   {
       z=0;
       for (i=0;i<n;i++)
       {
             if (a[i][j]==0)
             {
                 z=z+1;
             }

        }
        if(z>maxz)
        {
            maxz=z;
            ind=j;
        }

   }
cout<<j;
return 0;
}
