"""
    Stack merupakan salah satu implementasi dari Linked List. Stack merupakan kumpulan-kumpulan data yang 
menggunakan konsep LIFO ( Last In First Out ) atau FILO ( First In Last Out ), yaitu data yang paling 
terakhir dimasukan ke dalam stack merupakan data yang pertama kali keluar dari stack .
"""

class node:
    def __init__(self, element, next=None):
        self.element = element
        self.next = next

class llstack:
    def __init__(self):
        # refensi yg menujukan ke simpul pertama
        self.head = None
        # referensi yg menujukan ke simpul terakhir
        self.tail = None
        self.size = 0   # mula-mula stack kosong
    # memeriksa ukuran stack, kosong atau tdk
    def isempty(self):
        return self.size
