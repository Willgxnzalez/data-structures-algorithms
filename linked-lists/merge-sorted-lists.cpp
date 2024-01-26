// Very similar to merge step in mergesort algorithm
#include <iostream>

class Node {
public:
    int data;
    Node *next;
    Node() : data(0), next(nullptr) {}
    Node(int _data) : data(_data), next(nullptr) {}
    Node(int _data, Node *_next) : data(_data), next(_next) {}

    static void print(Node *L) {
        for (Node *p=L; p; p=p->next)
            std::cout << p->data << " ";
        std::cout << std::endl;
    }

    static void deleteList(Node *L) { /// All nodes share the same static delete method
        for (Node *p=L; p!=nullptr;) {
            Node *tmp = p;
            p = p->next;
            delete tmp;
        }
    }
};

Node * mergeTwoSortedLists(Node *L1, Node *L2) {
    if (!L1) return L2;
    if (!L2) return L1;

    Node * head = L1;
    if (L1->data > L2->data) {
        head = L2;
        L2 = L2->next;
    } else
        L1 = L1->next;
        
    Node *curr = head;
    while (L1 && L2) {
        if (L1->data > L2->data) {
            curr->next = L2;
            curr = L2;
            L2 = L2->next;
        } else {
            curr->next = L1;
            curr = L1;
            L1 = L1->next;
        }
    }
    // add the excess
    if (L1) curr->next = L1;
    if (L2) curr->next = L2;

    return head;
}

int main(int argc, char *argv[]) {
    Node *L1 = new Node(1, new Node(3, new Node(5, nullptr)));
    Node *L2 = new Node(2, new Node(4, new Node(6, nullptr)));
    Node *merged = mergeTwoSortedLists(L1, L2);
    Node::print(merged);
    Node::deleteList(merged);
}