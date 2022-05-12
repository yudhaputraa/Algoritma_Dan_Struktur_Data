"""
    Stack merupakan salah satu implementasi dari Linked List. Stack merupakan kumpulan-kumpulan data yang 
menggunakan konsep LIFO ( Last In First Out ) atau FILO ( First In Last Out ), yaitu data yang paling 
terakhir dimasukan ke dalam stack merupakan data yang pertama kali keluar dari stack .
"""

class node:
    def __init__(self, element, next=None):
        self.element = element
        self.next = next

