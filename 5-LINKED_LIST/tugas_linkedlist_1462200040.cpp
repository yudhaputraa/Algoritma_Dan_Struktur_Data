#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <conio.h>
#include <string.h>

using namespace std;

// Buat struktur Data untuk simpul dalam linked list
struct Mahasiswa {
    int nim, nilai;
    char nama[30], jurusan[30];
    Mahasiswa* next;
};

class Queue {
    private:
        Mahasiswa* head;
        Mahasiswa* tail;
        Mahasiswa* pos1;
        Mahasiswa* pos2;
        Mahasiswa* cur;
        Mahasiswa* del;

    public:
        Queue() {
            head = NULL;
            tail = NULL;
        }

        // Fungsi untuk menambahkan elemen ke dalam queue
        void enqueue() {
            system("cls");
            // deklarasi variabel
            Mahasiswa* temp = new Mahasiswa;

            // penginputan data mahasiswa
            cout << "Masukan NIM : ";
            cin >> temp->nim;
            cout<< "Masukan Nama : ";
            cin.ignore();
            cin.getline(temp->nama, 30);
            cout << "Masukan Jurusan : ";
            cin.getline(temp->jurusan, 30);
            cout << "Masukan Nilai : ";
            cin >> temp->nilai;

            // menyambungkan pointer baru ke list
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
        void hapus_data() {
            system("cls");
            Mahasiswa* temp = head;
            // mekihat data kosong atau ada
            if (head == NULL) {
                cout << "List kosong!\n"<<endl;
                return;
            }
            else {
                int dat_hap = NULL;
                cout << "Masukkan Data yang dihapus : ";
                cin >> dat_hap;

                // Deklarasi pointer untuk pencarian data yang akan dihapus
                Mahasiswa *pos1, *pos2;
                pos1 = head;
                pos2 = pos1;

                // mencari pada list sampai menemukan data yang akan dihapus
                while (pos1 != NULL)
                {
                    if (pos1->nim == dat_hap)
                        break;
                    pos2 = pos1;
                    pos1 = pos1->next;
                }

                // Jika data tidak ditemukan, tampilkan pesan dan keluar dari fungsi
                if (pos1 == NULL)
                {
                    cout << "Data yang dihapus tidak ditemukan\n";
                    return;
                }
                else
                {
                // Jika data yang dihapus berada pada head list, ubah head list menjadi node setelahnya
                    if (pos1 == head)
                        head = head->next;
                    else
                        // Jika data yang dihapus berada di tengah atau rear list, ubah pointer next pada node sebelumnya
                        pos2->next = pos1->next;

                    // Hapus node yang mengandung data yang dihapus
                    delete pos1;
                    cout << "Data berhasil dihapus\n";
                }
            }
        }

        // Fungsi untuk menampilkan elemen dalam queue
        void display() {
            system("cls");
            Mahasiswa* temp = head;
            while (temp != NULL) {
                cout << temp->nim << " ";
                cout << temp->nama << " ";
                cout << temp->jurusan << " ";
                cout << temp->nilai << " " << endl;
                temp = temp->next;
            }
            cout << endl;
            
            getch();
        }

        // Fungsi untuk mencari elemen dalam queue
        void search() {
            system("cls");
            if (head == NULL) //Memeriksa apakah linked list kosong
            {
                cout << "List kosong!\n";
                getch();
            }
            else
            {
                int dat_car = NULL;
                cout << "Masukkan NIM yang dicari : ";
                cin >> dat_car;

                Mahasiswa* temp = head;

                int i = 1;
                while (temp != NULL) {
                    if (temp->nim == dat_car) {
                        //Menampilkan informasi mengenai mahasiswa yang ditemukan
                        cout << "Data di temukan pada baris ke " << i << endl;
                        cout << "Nama : " << temp->nama << endl;
                        cout << "NIM : " << temp->nim << endl;
                        cout << "jurusan : " << temp->jurusan << endl;
                        cout << "Nilai : " << temp->nilai << endl;
                        getch();
                        return;
                    }
                    temp = temp->next;
                    i++;
                }
                cout << "Data tidak ditemukan\n";
                getch();
            }
        }

        void dequeue()
        {
            if (head == NULL) //Memeriksa apakah linked list kosong
            {
                cout << "List kosong!\n";
                getch();
            }
            else
            {
                del = head;
                head = head->next;
                del->next = NULL;
                delete del;
            }
        }

        // Fungsi untuk mengurutkan elemen dalam queue
        // void sort() {
        //     //?? deklarasi variabel pointer
        //     Mahasiswa *pos1, *pos2, *curr, *tmp;
        //     curr = new Mahasiswa;

        //     //~~ cek apakah linked list kosong
        //     if (head == NULL)
        //     {
        //         cout << "List kosong!\n";
        //         return;
        //     }
        //     else
        //     {
        //         //?? set pos1 sebagai node pertama
        //         pos1 = head->next;
        //         while (pos1 != NULL)
        //         {
        //             //^^ set curr sebagai posisi node saat ini
        //             curr = pos1;
        //             //^^ set pos2 sebagai node berikutnya
        //             pos2 = pos1->next;
        //             while (pos2 != NULL)
        //             {
        //                 //** jika data di posisi curr lebih besar dari data di posisi pos2
        //                 if (curr->nim > pos2->nim)
        //                     // set curr sebagai pos2
        //                     curr = pos2;
        //                 //** pindah ke node berikutnya
        //                 pos2 = pos2->next;
        //             }
        //             //^^ jika curr tidak sama dengan pos1 (data pada pos1 tidak paling kecil)
        //             if (curr != pos1)
        //             {
        //                 //** alokasi memori untuk tmp
        //                 tmp = new Mahasiswa;
        //                 //** simpan data di curr ke dalam tmp
        //                 tmp->nim = curr->nim;
        //                 strcpy(tmp->nama, curr->nama);
        //                 strcpy(tmp->jurusan, curr->jurusan);
        //                 tmp->nilai = curr->nilai;
        //                 //** tukar data pos1 dan curr
        //                 curr->nim = pos1->nim;
        //                 strcpy(curr->nama, pos1->nama);
        //                 strcpy(curr->jurusan, pos1->jurusan);
        //                 curr->nilai = pos1->nilai;
        //                 pos1->nim = tmp->nim;
        //                 strcpy(pos1->nama, tmp->nama);
        //                 strcpy(pos1->jurusan, tmp->jurusan);
        //                 pos1->nilai = tmp->nilai;
        //                 //** dealokasi memori untuk tmp
        //                 delete tmp;
        //             }
        //             //^^ pindah ke node berikutnya
        //             pos1 = pos1->next;
        //         }
        //         //?? cetak pesan berhasil diurutkan
        //          cout << "\nData berhasil diurutkan!" << endl;
        //         //??     tunggu inputan dari user
        //         getch();
        //     }
        // }
};

int main() {
    Queue Data_mahasiswa;

    string pilih;
    while (pilih != "7")
    {
        system("cls");
        cout << "|----------------|" << endl;
        cout << "|  Pilihan Menu  |" << endl;
        cout << "|----------------|" << endl;
        cout << "| 1. Isi Data    |" << endl;
        cout << "| 2. Lihat Data  |" << endl;
        cout << "| 3. Cari Data   |" << endl;
        cout << "| 4. Hapus Data  |" << endl;
        cout << "| 5. urut        |" << endl;
        cout << "| 5. dequeue     |" << endl;
        cout << "|----------------|" << endl;
        cout << "pilihan? = ";
        getline(cin, pilih);
        if (pilih == "1")
            Data_mahasiswa.enqueue();
        if (pilih == "2")
            Data_mahasiswa.display();
        if (pilih == "3")
            Data_mahasiswa.search();
        if (pilih == "4")
            Data_mahasiswa.hapus_data();
        if (pilih == "5")
            Data_mahasiswa.display();
        if (pilih == "6")
            Data_mahasiswa.dequeue();
    }
    return 0;
}