
// C++ program to find height of tree
#include <bits/stdc++.h>
using namespace std;

class node 
{ 
    public:
    int data; 
    node* left; 
    node* right; 
}; 

int maxDepth(node* node) 
{ 
    if (node == NULL) 
        return -1;
    else
    { 
        
        int leftDepth = maxDepth(node->left); 
        int rightDepth = maxDepth(node->right); 
    
        /* use the larger one */
        if (leftDepth > rightDepth) 
            return(leftDepth + 1); 
        else return(rightDepth + 1); 
    } 
} 


node* newNode(int data) 
{ 
    node* Node = new node();
    Node->data = data; 
    Node->left = NULL; 
    Node->right = NULL; 
    
    return(Node); 
} 
    
// main code    
int main() 
{ 
    node *root = newNode(10); 

    root->left = newNode(21); 
    root->right = newNode(32); 
    root->left->left = newNode(43); 
    root->left->right = newNode(55); 
    
    cout << "Height of tree is " << maxDepth(root); 
    return 0; 
} 

// This code is contributed by Amit Sandeep Raj