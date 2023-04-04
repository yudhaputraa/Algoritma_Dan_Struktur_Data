#include <iostrem>
#include <string>

using namespace std;

// deklarasi single linked list
struct buku{

    // komponen / member
    string judul, pengarang;
    int tahunTerbit;

    buku *next;
}

int main(){

    // inisialisasi single linked list
    buku *node1, *node2, *node3;

    // ini lebih ke posuderal
    //node1 = (buku*) malloc(sizeof(buku));
    node1 = new buku();
    node2 = new buku();
    node3 = new buku();
}