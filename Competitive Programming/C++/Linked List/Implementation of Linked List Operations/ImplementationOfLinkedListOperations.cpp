#include <iostream>
using namespace std;

void insertAtTheBeginning();
void insertInBetween();
void insertAtTheEnd();
void deleteFirst();
void deleteLast();
void deleteAny();
void search();
void print();

class Node
{
public:
    int data;
    Node *next;
    Node()
    {
        data = 0;
        next = NULL;
    }
};

Node *head = NULL;

int main()
{
    int choice = 0;
    while (choice != 8)
    {
        cout << "*****MENU*****" << endl;
        cout << "1.Insert at the beginning\n2. Insert in between\n3. Insert at the end\n4. Delete first node\n5. Delete last node\n6. Delete a node at any position\n7. Search for a node\n8. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;
        switch (choice)
        {
        case 1:
        {
            insertAtTheBeginning();
            break;
        }
        case 2:
        {
            insertInBetween();
            break;
        }
        case 3:
        {
            insertAtTheEnd();
            break;
        }
        case 4:
        {
            deleteFirst();
            break;
        }
        case 5:
        {
            deleteLast();
            break;
        }
        case 6:
        {
            deleteAny();
            break;
        }
        case 7:
        {
            search();
            break;
        }
        case 8:
        {
            exit(0);
            break;
        }
        default:
            cout << "Invalid Input. Please try again" << endl;
        }
    }
}

void insertAtTheBeginning()
{
    Node *firstNode = NULL;
}