#include <iostream>

using namespace std;

// deklarasi single linked list
struct buku{

    // komponen / member
    string judul, pengarang;
    int tahunTerbit;

    buku *next;
};

int main(){

    // inisialisasi single linked list
    buku *node1, *node2, *node3;

    // ini lebih ke posuderal
    //node1 = (buku*) malloc(sizeof(buku));
    node1 = new buku();
    node2 = new buku();
    node3 = new buku();

    // pengisian node 1
    node1->judul = "Matematika";
    node1->pengarang = "Ahli Matematika";
    node1->tahunTerbit = 1995;
    node1->next = node2;

    // pengisian node 2
    node2->judul = "jatuh nya tandon ke hati";
    node2->pengarang = "lalita";
    node2->tahunTerbit = 2034;
    node2->next = node3;

    // pengisian node 3
    node3->judul = "pop mie ku tergantikan oleh padang";
    node3->pengarang = "sugianto";
    node3->tahunTerbit = 1374;
    node3->next = NULL;

    buku *cur;
    cur = node1;
    while(cur != NULL){
        cout << "Judul Buku : " << cur->judul<<endl;
        cout << "Pengarang Buku : " << cur->pengarang<<endl;
        cout << "Tahun Terbit Buku : " << cur->tahunTerbit<<endl;

        cur = cur->next;
    }

}