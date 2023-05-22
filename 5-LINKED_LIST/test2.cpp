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

int maksimalAnLiLi = 5;
Mahasiswa *head, *tail, *cur, *del;

int countlinkedlist(){
    if(head == NULL){
        return 0;
    }else{
        int banyak = 0;
        cur = head;
        while(cur != )
    }
}