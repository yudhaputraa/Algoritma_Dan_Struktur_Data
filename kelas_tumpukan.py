"""
    Pembahasan Stack Algoritma stack merupakan struktur data yang mengimplementasi dari aturan 
LIFO (Last  In First Out). Jadi elemen yang dimasukan terakhir berada di atas (top). Stack 
dapat  direpresentasikan dengan type data array, pointer (list), atau cursor. Operasi – operasi 
yang terdapat pada Stack :  1. Create, membuat stack baru (dengan nilai 0)  2. IsEmpty, mengecek 
apakah stack kosong (null)  3. IsFull, mengecek apakah stack penuh(null)  4. Push, memasukan elemen 
pada stack  5. Pop, menghapus elemen pada stack  6. Dan lain‐lain silakan di eksplorasi. Jika stack
direpresentasikan  dengan  array,  maka  elemen  dari  stack  S[1..Top]. s[1] merupakan elemen dasar 
dari stack dan S[Top] merupakan elemen puncak atau  paling atas dari stack. jika nilai dari Top = 0 
berarti stack kosong, sebaliknya jika Top = Max berarti  stack  penuh.  Dimana  Max  merupakan 
jumlah  elemen  yang  dapat  ditampung dalam stack.
    Stack atau Tumpukan adalah suatu struktur data yang terbentuk dari barisan hingga yang terurut 
dari satuan data. Pada Stack, penambahan dan penghapusan elemennya hanya dapat dilakukan pada satu 
posisi, yaitu posisi akhir stack. Posisi ini disebut Puncak atau Top dari stack
    Stack biasa digunakan dalam mengontrol operasi dalam sebuah sistem operasi. Selain itu stack 
juga merupakan algoritma yang baik yang dapat digunakan untuk membuat phaser (membaca urutan operasi 
dari sebuah persamaan matematika).
"""

# Untuk stack mengimplementasi struktur data stack menggunakan list, anda dapat menulis
# kode seperti berikut :

class stack:
    def __init__(self):
        # membuat stack kosong
        self.__data = []
    # metode utk mengetahui jumblah elemn stack
    def __len__(self):
        return len(self.__data)
    # metode utk memeriksa stack, kosong atau tdk
    def isempty(self):
        return len(self.__data) == 0
    # metode utk menambah elemen
    def push(self, element):
        self.__data.append(element)
    # metode utk mengtahui elemen paling atas
    def top(self):
        if self.isempty():
            raise Exception('Stack kosong')
        return self.__data[-1]
    # metode utk mengambil elemen paling atas
    def pop(self):
        if self.isempty():
            raise Exception('Stack kosong')
        return self.__data.pop()
    def __repr__(self):
        return repr(self.__data)


# membuat objek dari kelas stack
s = stack()

# menambahkan elemen ke dalam stack
s.push('python')

# menampilkan isi stack
print(s)

# menambah kembali ua elemen baru ke dalam stack
s.push('Ruby')
s.push('PHP')
print(s)

# mendapatkan elemen terakhir (paling atas)
print(s.top())

# menampilkan isi stack
# setelah pemanggilan metode stop()
print(s)

# mengambil elemen terakhir (paling atas)
print(s.pop())

# menampilkan isi stack
# setelah pemanggilan metode pop()
print(s)

# mendapatkan jumblah elemn di dalam stack
print(len(s))

"""
## Penjelasan
    Tumpukan(Stack) adalah suatu struktur data menerapakan konsep LIFO(Last in firs out). Artinya, data
yg terakhir ditambahkan ke dalam stack akan berada di posisi terakhir (atau paling atas jika Anda 
membayangkan elemen-elemen stack tersusun secara vertikal); dan ketika proses pengambilan, data 
terakhir tersebut akan diambil pertama kali.

Pada kelas stack di atas, kita mengimplementasikan metode-metode berikut:

- isempty(), digunakan untuk memeriksa apakah stack kosong atau tidak.

- __len__(), metode ini perlu diimplementasikan agar objek dari kelas stack dapat dihitung jumlah 
elemennya menggunakan metode len().

- push(), digunakan untuk menambah elemen baru ke dalam stack pada posisi terakhir.

- top(), digunakan untuk mendapatkan elemen yang terdapat pada posisi terakhir tanpa menghapus 
elemen tersebut.

- pop(), digunakan untuk mengambil elemen terakhir dan menghapusnya dari dalam stack.

- __repr__(), metode ini perlu diimplementasikan agar elemen-elemen yang terdapat di dalam objek 
stack dapat ditampilkan dalam bentuk string.
"""