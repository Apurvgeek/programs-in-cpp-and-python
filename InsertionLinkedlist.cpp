#include <iostream>
using namespace std;

class Node
{
    public:
    int data;
    Node *next;

};

Node *insert(Node*head, int data)
{
    Node*ptr = new Node();
    ptr ->next = head;
    ptr ->data = data;
    return ptr;
}

void linkedlistTraversal(Node *ptr)
{
    while(ptr != NULL)
    {
        cout<<"Element:"<<ptr->data<<endl;
        ptr = ptr->next;
    }
}

int main()
{
    int n,data,i;
    cout<<"Enter the number of nodes : ";
    cin>>n;
    Node *head = new Node();
    head = NULL;

    for ( i = 0; i < n; i++)
    {
        cin>>data;
        head = insert(head,data);
    }
    linkedlistTraversal(head);
    return 0;
    
}