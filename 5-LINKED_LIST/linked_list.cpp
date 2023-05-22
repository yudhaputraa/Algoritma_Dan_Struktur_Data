#include <iostream>
#include <stdio.h>
#include <conio.h>
#include <string.h>

using namespace std;

// Buat struktur data untuk simpul dalam linked list
struct Node {
    int data;
    Node* next;
};

class Queue {
    private:
        Node* head;
        Node* tail;

    public:
        Queue() {
            head = NULL;
            tail = NULL;
        }

        // Fungsi untuk menambahkan elemen ke dalam queue
        void enqueue(int value) {
            Node* temp = new Node;
            temp->data = value;
            temp->next = NULL;

            if (head == NULL && tail == NULL) {
                head = tail = temp;
            }
            else {
                tail->next = temp;
                tail = temp;
            }
        }

        // Fungsi untuk menghapus elemen dari queue
        void dequeue() {
            Node* temp = head;
            if (head == NULL) {
                return;
            }
            if (head == tail) {
                head = tail = NULL;
            }
            else {
                head = head->next;
            }
            delete temp;
        }

        // Fungsi untuk menampilkan elemen dalam queue
        void display() {
            Node* temp = head;
            while (temp != NULL) {
                cout << temp->data << " ";
                temp = temp->next;
            }
            cout << endl;
        }
};

int main() {
    Queue q;

    q.enqueue(1);
    q.enqueue(2);
    q.enqueue(3);
    q.enqueue(4);
    q.enqueue(5);

    q.display();

    q.dequeue();
    q.dequeue();

    q.display();

    return 0;
}