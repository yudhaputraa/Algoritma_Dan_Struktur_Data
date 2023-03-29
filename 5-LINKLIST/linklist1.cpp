#include <iostream>

using namespace std;

// definisi struktur node
struct Node {
    int data;
    Node* next;
};

// fungsi untuk menambahkan node di awal linked list
void tambahDepan(Node** head, int newData) {
    // membuat node baru
    Node* newNode = new Node;
    newNode->data = newData;
    newNode->next = (*head);
    // mengubah head menjadi node baru
    (*head) = newNode;
}

// fungsi untuk mencetak linked list
void cetakList(Node* node) {
    while (node != NULL) {
        cout << node->data << " ";
        node = node->next;
    }
    cout << endl;
}

int main() {
    // inisialisasi linked list
    Node* head = NULL;

    // menambahkan node baru di awal linked list
    tambahDepan(&head, 3);
    tambahDepan(&head, 5);
    tambahDepan(&head, 7);
    tambahDepan(&head, 9);

    // mencetak linked list
    cetakList(head);

    return 0;
}
