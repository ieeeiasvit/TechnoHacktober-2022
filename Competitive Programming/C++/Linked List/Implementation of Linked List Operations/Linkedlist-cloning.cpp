#include <bits/stdc++.h>
using namespace std;

struct Node
{
    int data;
    Node *next,*random;
    Node(int x)
    {
        data = x;
        next = random = NULL;
    }
};
Node *clone(Node *head)
{
    for(Node *curr = head ;curr!=NULL;curr=curr->next)
    {
        Node *temp = curr->next ;
        Node *temp1 = new Node(curr->data);
        curr->next = temp1 ;
        temp1->next = temp ;
    }
    for(Node *curr= head ;curr!=NULL;curr=curr->next->next)
    {
        curr->next->random = (curr->random!=NULL)? (curr->random->next) : NULL ;
    }
    Node *curr = head ;
    Node *curr1 = head->next ;
    while(curr!=NULL && curr1!=NULL)
    {
        curr->next = (curr->next!=NULL)?(curr->next->next):NULL ;
        curr1->next = (curr1->next!=NULL)?(curr1->next->next):NULL ;
        curr=curr->next ;
        curr1=curr1->next ;
    }
    return head->next ;
}
void print(Node *start)
{
    Node *ptr = start;
    while (ptr)
    {
        cout << "Data = " << ptr->data << ", Random  = "<< ptr->random->data << endl;
        ptr = ptr->next;
    }
}
int main()
{
	Node* head = new Node(10);
    head->next = new Node(5);
    head->next->next = new Node(20);
    head->next->next->next = new Node(15);
    head->next->next->next->next = new Node(20);

    head->random = head->next->next;
    head->next->random=head->next->next->next;
    head->next->next->random=head;
    head->next->next->next->random=head->next->next;
    head->next->next->next->next->random=head->next->next->next;

    cout << "Original list : \n";
    print(head);

    cout << "\nCloned list : \n";
    Node *cloned_list = clone(head);
    print(cloned_list);

    return 0;
}
