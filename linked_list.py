"""
Apa yang dimaksud dengan linked list?
    Linked List adalah suatu struktur data linier. Berbeda dengan array yang juga merupakan struktur 
data linier dan tipe data komposit, linked list dibentuk secara dinamik. Pada saat awal program dijalankan 
elemen linked list belum data. Elemen linked list (disebut node) dibentuk sambil jalan sesuai instruksi.

Linked list digunakan untuk apa?
    Linked list adalah sekumpulan elemen bertipe sama, yang mempunyai keterurutan tertentu, yang setiap 
elemennya terdiri dari dua bagian Linked list juga merupakan suatu cara untuk menyimpan data dengan struktur 
sehingga dapat secara otomatis menciptakan suatu tempat baru untuk menyimpan data yangdiperlukan.
"""

from xml.dom.minidom import Element


class node:
    def __init__(self, element, next=None):
        self.element = element
        self.next = next

class linkedlist:
    def __init__(self):
        # referensi yang menunjukan ke simpul pertama
        self.head = None
        # referensi yg menunjukan simplkan terakhir
        self.tail = None
        self.size = 0   # mula-mula list kosong
    # memeriksa ukuran list
    def isemply(self):
        return self.size == 0
    # menambahkan simpulan pd posisi pertama
    def addfist(self, elemen):
        # membuat simpulan baru ( newnode.next menujuk ke head )
        newnode = node(elemen, self.head)
        # head menunjuk ke simpul baru
        self.head = newnode
        # menambah ukuran list
        self.size += 1
        # jika list hanya berisi satu simpul
        if self.tail == None:
            self.tail = self.head
    # mendapatkan elemen pd simpul pertama
    def getfirst(self):
        if self.isemply():
            return None
        else:
            return self.head.element
    # menghapus simpul pertama
    def removefirst(self):
        if not self.isemply():
            temp = self.head
            self.head = self.head.next
            self.size -= 1 # mengurangi ukuran list
            del temp # opsional
    # menambahkan simpul pd posisi terakhir
    def addlast(self, element):
        # membuat simpul baru (newnode.next berisi None)
        newnode = node(element)
        if self.tail == None: # jika list masih kosong
            self.head = newnode # head menunjuk ke simpul baru
            self.tail = self.head # tail menujuk ke head
        else: # jika list sudah berisi simpul
            # menghubungkan simpul terakhir dgn simpul baru
            self.tail.next = newnode
            # memindah tail utk menujuk ke simpul baru
            self.tail = self.tail.next
        self.size += 1
    # mendapatkan elemen pd simpul terakhir
    def getlast(self):
        if self.isemply():
            return None
        else:
            return self.tail.element
        
    # menghapus simpul terakhir
    def removelast(self):
        if not self.isemply():
            if self.size == 1:
                temp = self.head
                self.head = None
                self.tail = None
                self.size = 0
                del temp
            else:
                current = self.head
                while current.next != self.tail:
                    current = current.next
                temp = self.tail
                self.tail = current
                self.tail.next = None
                self.size -= 1
                del temp
    # menampilkan elemen-elemen pd setiap simpul di dalam list
    def __str__(self):
        s = '['
        current = self.head
        while current != None:
            s += str(current.element)
            if current != self.tail:
                s += ', '
            current = current.next
        s += ']'
        return s
    def __repr__(self):
        return self.__str__()

# membuat objek dari kelas linkedlist
llist = linkedlist()

# menambak elemen menggunakan addfirst()
llist.addfist('Python')

# menambak elemen menggunakan addlast()
llist.addlast('Ruby')

# menampilkan elemen-elemen di dalam list
print(llist)

print("#"*10)
# menambah elemen menggunakan addlast()
llist.addfist('C++')

# menambah elemen menggunakan addlast()
llist.addlast('PHP')
llist.addlast('Java')
llist.addlast('Perl')

print(llist)

print("#"*10)
# mendapatkan elemen pertama
print(llist.getfirst())

print("#"*10)
# mendapatkan elemen terakhir
print(llist.getlast())

print("#"*10)
# menghapus simpul pertama
llist.removefirst()

print(llist)

print("#"*10)
# menghapus simpul terakhir
llist.removelast()

print(llist)