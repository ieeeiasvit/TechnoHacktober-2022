#include<iostream>
using namespace std ;

struct Node
{
    int data ;
    Node *next ;
    Node(int x)
    {
        data = x ;
        next = NULL ;
    }
};

Node *reverselist(Node *head)
{
    /*if(head==NULL)
    {
        return NULL ;
    }
    if(head->next==NULL)
    {
        return head ;
    }*/
    Node *curr = head ;
    Node *prev =NULL;
    //head->next = NULL;

    while(curr!=NULL)
    {
        Node *temp = curr->next ;
        curr->next = prev ;
        prev = curr ;
        curr = temp ;
    }
    return prev ;
}
void printlist(Node *head)
{
    while(head!=NULL)
    {
        cout<<head->data<<" ";
        head = head->next ;
    }
}
int main()
{
    Node *head = new Node(10);
    head->next = new Node(20);
    head->next->next= new Node(30);
    printlist(head);
    head = reverselist(head);
    printlist(head);
}
