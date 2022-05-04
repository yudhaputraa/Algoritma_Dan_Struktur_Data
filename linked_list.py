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


## PENJELASAN
"""
Dalam kelas linkedlist di atas, kita hanya mengimplementasikan metode-metode berikut:
● isempty(), digunakan untuk memeriksa apakah list kosong atau tidak.
● addfirst(), digunakan untuk menambah simpul baru ke dalam list pada posisi pertama.
● getfirst(), digunakan untuk mendapatkan elemen yang terdapat pada simpul pertama.
● removefirst(), digunakan untuk menghapus simpul pertama. 
● addlast(), digunakan untuk menambah simpul baru ke dalam list pada posisi terakhir.
● getlast(), digunakan untuk mendapatkan elemen yang terdapat pada simpul terakhir.
● removelast(), digunakan untuk menghapus simpul terakhir. 
● __str__(), digunakan untuk menampilkan elemen-elemen list dalam bentuk string.
● repr___(), digunakan untuk merepresentasikan objek dari kelas linkedlist sebagai string. 
Metode ini sebenarnya memanggil metode __str__(). Dengan mengimplementasikan metode repr (), 
Anda dapat memperoleh nilai yang dikembalikan oleh metode __str__() dengan memanggil fungsi repr();
atau cukup dengan memanggil nama objek dari kelas linkedlist. Dengan demikian, elemen-elemen di 
dalam list dapat ditampilkan menggunakan perintah repr (1list) atau llist (dengan asumsi llist 
adalah referensi yang menunjuk ke objek dari kelas linkedlist).

    Anda dapat mengembangkan sendiri kelas linkedlist di atas dengan cara mengimplementasikan 
metode-metode lain yang diperlukan, misalnya:
● contains(element), metode untuk memeriksa apakah metode contains(element), element ada di 
dalam list atau tidak;
● indexof(element), metode untuk mengembalikan indeks dari simpul yang berisi element;
● getelement(index), metode untuk mengembalikan objek yang terkandung di dalam simpul pada 
posisi ke-index;
● setelement(index, element), metode untuk mengubah objek yang terkandung di dalam simpul 
pada posisi ke-index; add(index, element), metode untuk menyisipkan simpul baru pada posisi 
ke-index.
● remove(index), metode untuk menghapus simpul yang terdapat pada posisi ke-index.
● clear(), metode untuk menghapus semua simpul di dalam list; dan lain-lain.

Selain metode, dalam kelas linkedlist kita juga mendefinisikan atribut-atribut berikut:
● head(kepala), referensi yang digunakan untuk menunjuk ke simpul pertama di dalam list.
● tail(ekor), referensi yang digunakan untuk menunjuk ke simpul terakhir di dalam list.
● size, digunakan untuk menyatakan jumlah simpul di dalam list.
"""

## Implementasi metode addfirst()
"""
Untuk menambah simpul baru di posisi pertama list, mula-mula kita perlu membuat simpul yang akan ditambahkan 
dengan cara membuat objek dari kelas node. Dalam contoh ini, kita menamai objek tersebut dengan nama newnode. 
Atribut next dari objek newnode perlu diarahkan ke objek node yang sedang ditunjuk oleh head. Melalui cara 
seperti ini, newnode akan berada di awal list.

newnode = node (element, self.head)

Selanjutnya, kita perlu mengubah referensi head untuk menunjuk ke newnode. Ini menyatakan bahwa simpul 
awal di dalam list telah diganti dengan newnode.

self.head = newnode

Penambahan simpul juga akan mempengaruhi jumlah simpul di dalam list (bertambah satu). Kita dapat menambah 
jumlah atau ukuran simpul di dalam list menggunakan baris kode berikut:

self.size += 1 +

Jika sebelum pemanggilan metode addfirst() list masih dalam keadaan kosong, maka newnode akan berperan 
sebagai satu-satunya simpul yang terdapat di dalam list. Oleh karena itu, referensi tail juga harus diarahkan 
ke objek yang sedang ditunjuk oleh referensi head. Artinya, newnode akan berperan sebagai simpul pertama dan 
juga simpul terakhir.

28 if self.tail = None: 
    self.tail = self.head
"""

## Implementasi metode getfirst()
"""
Metode getfirst() akan mengembalikan elemen atau objek yang terkandung pada simpul pertama. Jika list 
masih dalam keadaan kosong, pemanggilan getfirst() tidak akan menghasilkan apa-apa (direpresentasikan dengan 
nilai None).
"""

## Implementasi metode removefirst()
"""
Metode removefirst() digunakan untuk menghapus simpul pertama. Proses penghapusan ini akan menyebabkan 
referensi head berpindah ke simpul berikutnya (jika ada). Sebelum dihapus, Anda dapat menampung terlebih 
dahulu simpul bersangkutan ke dalam variabel temp, kemudian menghapusnya secara eksplisit dengan perintah 
del. Ini bersifat opsional; bisa dilakukan, bisa juga tidak. Alasannya, interpreter Python secara otomatis 
akan membuang objekobjek yang sudah tidak diacu oleh referensi manapun.
"""

## Implementasi metode addlast()
"""
Metode addlast() digunakan untuk menambah simpul baru ke dalam list pada posisi paling akhir. Jika pada 
saat pemanggilan metode addlast() list masih dalam keadaan kosong, maka simpul baru yang ditambahkan akan 
menjadi satu-satunya simpul di dalam list. Artinya, simpul tersebut akan berperan sebagai simpul pertama 
(ditunjuk oleh referensi head) dan simpul terakhir (ditunjuk oleh referensi tail). Jika list sudah memiliki 
simpul, pemanggilan addlast() akan mengaitkan simpul terakhir ke simpul baru melalui baris kode berikut:

self.tail.next = newnode

Setelah itu, referensi tail dipindah untuk menunjuk ke simpul baru melalui kode berikut: m

self.tail = self.tail.next

Terakhir, metode addlast () akan mengubah jumlah simpul di dalam list melalui kode berikut:

self.size += 1
"""

## Implementasi metode getlast()
"""
Metode getlast() akan mengembalikan elemen atau objek yang terkandung pada simpul terakhir. Jika list 
belum memiliki simpul, pemanggilan getlast () akan menghasilkan nilai None.
"""