/*00 01 02 03 04
  10 11 12 13 14
  20 21 22 23 24
  30 31 32 33 34
*/
#include<iostream>


using namespace std;

void spiral_print(int arr[100][100],int m,int n)
{
    int startRow=0;
    int startCol=0;
    int endRow=m-1;//3
    int endCol=n-1;//4
    while(startCol<=endCol && startRow<=endRow)
    {
        //printing 00 01 02 03 04
        for(int i=startCol;i<=endCol;i++)
        {
            cout<<arr[startRow][i]<<" ";
        }
        startRow++;

        // printing 14 24 34
         for(int i=startRow;i<=endRow;i++)
        {
            cout<<arr[i][endCol]<<" ";
        }
        endCol--;

        //printing 33 32 31 30
        if(endRow > startRow)
        {

        for (int i=endCol;i>=startCol;i--)
        {
            cout<<arr[endRow][i]<<" ";
        }
        }
        endRow--;

        //printing 20 10
        if (endCol > startCol)
        for (int i=endRow;i>=startRow;i--)
        {
            cout<<arr[i][startCol]<<" ";
        }
        startCol++;
        //1st Round Complete startRow=1;endCol=3;endRow=2;startCol=1;
        //repeat above
       }
}

int main()
{
    int a[100][100]={0};
    int m,n;
    cin>> m >> n;

    int val=1;
    for(int i=0;i<=m-1;i++)
    {
        for(int j=0;j<=n-1;j++)
        {
            a[i][j]=val;
            val++;
           cout<<a[i][j]<<" ";
        }
        cout<<endl;
    }
spiral_print(a,m,n);
return 0;
}
