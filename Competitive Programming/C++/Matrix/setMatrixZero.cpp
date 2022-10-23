#include <bits/stdc++.h> 
using namespace std;

void setZeros(vector<vector<int>> &vect)
{
    int x,y;
	for (int i = 0; i < vect.size(); i++)
    {
        for (int j = 0; j < vect[i].size(); j++)
        {
            if(vect[i][j]==0)
            {
                x=i;
                y=j;

            }
        }  
        for(int k=0;k<=x;k++)
        {
            vect[x][k]=0;
        }
        for(int k=0;k<=y;k++)
        {
            vect[k][y]=0;
        }
   
        
    }
}



int main(int argc, char const *argv[])
{
    vector<vector<int>>vect={{2,4,1},{1,2,0}};

  
    setZeros(vect);

    for (int i = 0; i < vect.size(); i++)
    {
        for (int j = 0; j < vect[i].size(); j++)
        {
            cout << vect[i][j] << " ";
        }    
        cout << endl;
    }

    return 0;
}
