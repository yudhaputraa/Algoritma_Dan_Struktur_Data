"""
    Pengertian queue adalah sekumpulan data yang mana penambahan elemen hanya bisa dilakukan pada 
suatu ujung yang disebut sisi belakang (rear), dan penghapusan (pengambilan elemen) dilakukan 
lewat ujung lain. Contoh queue paling sederhana dapat dilihat pada antrian.
    Queue (antrian) adalah salah satu list linier dari struktur data yang beroperasi dengan cara 
First In First Out (FIFO) yaitu elemen pertama yang masuk merupakan elemen yang pertama keluar. 
Data-data di dalam antrian dapat bertipe integer, real, record dalam bentuk sederhana atau 
terstruktur.
    Queue digunakan seperti halnya antrian jika antrian pertama sudah di jalankan maka antrian 
tersebut akan di hapus dan ganti antrian berikutnya. Array berbeda dengan queue. Jika semisal kita 
gunakan array pada index 0 nilai pada array akan tetap.
"""

class queue:
    def __init__(self):
        self.__data = []
        self.__size = 0
        self.__font = 0 # posisi elemen queue
    # metode utk mengtahui jumblah elemen queue
    def __len__(self):
        return self.__size
    # metode utk memeriksa queue, kosong atau tdk
    def isemply(self):
        return self.__size == 0
    # metode utk mendapatkan elemen pertama
    def first(self):
        if self.isemply():
            raise Exception('queue kosong....')
        return self.__data[self.__font]
    # metode utk menambah elemen ke dalam queue
    def enqueue(self, element):
        self.__data.append(element)
        self.__size += 1
    # metode utk mengambil elemen pertama
    def dequeue(self):
        if self.isemply():
            raise Exception('queue kosong....')
        result = self.__data[self.__font]
        del self.__data[self.__font]
        self.__size -= 1
        return result
    # metode utk menampilkan elemen queue
    def __repr__(self):
        return repr(self.__data)


# membuat objek dari kelas queue
q = queue()

# menambahkan elemen ke dalam queue
q.enqueue('Python')
q.enqueue('Ruby')
q.enqueue('PHP')
q.enqueue('Perl')

# menampilkan isi queue
print(q)

# menampilkan jumlah elemen
print(len(q))

# mendapatkan elemen pertama
print(q.first())

print("#"*10)
# menampilan isi queue
# setelah pemanggilan metode first()
print(q)

# mengambil elemen pertama
print(q.dequeue())

print("#"*10)
# menampilan isi queue
# setelah pemanggilan metode dequeue()
print(q)

# menampilkan jumlah elemen
print(len(q))

# mengmbil kembali elemen pertama
print(q.dequeue())
print(q)
print(len(q))

"""
## Penjelasan

    Antrian (queue) merupakan struktur data yang menerapkan konsep FIFO (first in first out). 
Data atau elemen yang pertama ditambahkan ke dalam queue akan diambil pertama kali juga.

Pada kelas queue di atas, kita mengimplementasikan metode-metode berikut:

- isempty(), digunakan untuk memeriksa apakah queue kosong atau tidak.

- __len__(), metode ini perlu diimplementasikan agar objek dari kelas queue dapat dihitung jumlah 
elemennya menggunakan metode len().

- enqueue(), digunakan untuk menambah elemen baru ke dalam queue pada posisi terakhir.

- first(), digunakan untuk mendapatkan elemen yang terdapat pada posisi pertama tanpa menghapus 
elemen tersebut. .

- dequeue(), digunakan untuk mengambil elemen terakhir dan menghapusnya dari dalam queue.

- __repr__(), metode ini perlu diimplementasikan agar elemenelemen yang terdapat di dalam objek 
queue dapat ditampilkan dalam bentuk string.
"""