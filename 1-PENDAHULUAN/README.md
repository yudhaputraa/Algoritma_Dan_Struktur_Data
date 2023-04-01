# Catatan
## Pendahuluan
Struktur Data dan Algoritma merupakan salah satu materi pada Teknik Informatika yang merupakan pendahuluan atau langkah awal untuk menuju ke pemrograman berorientasi objek

Asal mula kata ‘algoritma’ adalah dari kata ‘algorism’ dalam kamus Webster tahun 1957 yang berarti proses menghitung dengan angka arab. Algorism merupakan nama penulis buku Arab yang berjudul “The book of restoration and reduction”. Kata algorism kemudian berubah menjadi kata algoritm agar tidak diinterpretasikan dengan aritmatik. Akhirnya dalam bahasa Indonesia kata algorithm diserap menjadi algoritma.

Menurut Donald E. Knuth dalam buku “The Art of Computer
Programming” , algoritma mempunyai lima ciri yaitu;
1. Algoritma harus ada berhentinya setelah menyelesaikan sejumlah langkah.
2. Setiap langkah harus didefiniskan dengan tepat dan tidak mendua.
3. Algoritma memiliki masukan sebanyak 0 sampai n
4. Algoritma memiliki keluaran sebanyak 1 sampai n
5. Setiap langkah harus efektif (cepat dan hemat memory).

### Tujuan dari algoritma yaitu
1. membuat penyelesaian masalah secara cepat dan efisien.
2. Algoritma yang baik harus bersifat efisien waktu dan penggunaan memori komputer. Hasil akhir fase penyelesaian masalah adalah penyelesaian dalam bentuk algoritma.
3. memberikan petunjuk tentang langkah-langkah logika penyelesaian masalah dalam bentuk yang mudah dipahami nalar manusia sebagai acuan yang membantu dalam mengembangkan program komputer. Pemahaman terhadap algoritma akan mencegah sejak dini kemungkinan terjadinya kesalahan logika pada program komputer yang dikembangkan.


### Arti Penting Algoritma
fase penyelesaian masalah (problem solving phase)
1. Menganalisa dan memahami suatu permasalahan untuk menemukan kemungkinan penyelesaiannya
2. Merancang algoritma yang merupakan pola pikir terstruktur yang berisi tahap-tahap penyelesaian suatu permasalahan
3. Membuat program komputer yaitu mengubah kode dari algoritma yang telah dibuat ke dalam pernyataan-pernyataan yang sesuai dengan bahasa pemrograman yang dipakai [coding]
4. Menjalankan program secara rutin untuk menemukan kesalahan penulisan suatu pernyataan dalam program [testing] dan menemukan kesalahan program. Kesalahan yang ditemukan diperbaiki sampai tidak muncul kesalahan lagi [debugging]
5. Melakukan dokumentasi terhadap setiap langkah yang dilakukan [documentation]
fase implementasi (implementation phase)

### Kriteria yang harus dipenuhi oleh prosedur
penyelesaian masalah dengan algoritma:
1. Setiap langkah harus bersifat pasti atau tertentu(definite)
2. Terdapat setidaknya satu keluaran (output)
3. Terstruktur dan sistematis
4. Memiliki kriteria untuk menghentikan proses

### Syarat-syarat yang harus dipenuhi oleh suatu algoritma:
1. Logika prosedur pada algoritma harus cukup mudah dipahami nalar manusia
2. Validitas prosedur pada algoritma dapat ditelusuri dengan mudah
3. Tidak menimbulkan kerancuan interpretasi bagi orang lain
4. Prosedur pada algoritma harus cukup mudah dikonversi ke program komputer
5. Prosedur pada algoritma tidak terpengaruh atau tergantung pada bahasa pemrograman apa pun

### Program terstruktur memberikan beberapa keuntungan, antara lain :
1. Penulisan program menjadi lebih teratur
2. Program tersusun secara sistematis
3. Program tersusun secara terstruktur
4. Lebih mudah dipahami
5. Urutan atau alur proses dalam program menjadi sederhana dan mudah dipahami

## Struktur Dasar Algoritma
Struktur Dasar Algoritma:
1. Struktur Urutan; Terdiri dari beberapa aksi yang dikerjakan secara urut
dari atas kebawah atau dari kiri ke kanan.
2. Struktur Pilihan/Cabang, aksi dikerjakan jika sesuai kondisi pilihannya.
a. Struktur IF, aksi dikerjakan jika salah satu dari dua pilihan terpenuhi
b. Struktur CASE,aksi dipilih jika salah satu diantara beberapa pilihan
terpenuhi
3. Struktur Perulangan, aksi dikerjakan secara berulang-ulang, yang terdiri
dari
a. Struktur FOR, aksi diulangi sebanyak n kali
b.Struktur REPEAT, aksi diulangi sampai kondisi benar
c. Struktur WHILE, aksi diulangi selama kondisi benar
Kondisi adalah pernyataan logika yang dapat dievalusi benar atau salah.
Contohnya:
Apakah A>0 ; pernyataan logika
Apakah A ; bukan pernyataan logika
Apakah kekanan ; pernyataan logika
Apakah B=10 ; pernyataan logika

## Pengelompokan struktur proses dalam algoritma:
### Proses urutan (sequence)
1. Prosedur proses dalam algoritma yang dilakukan secara urut langkah demi langkah.
2. Sebuah urutan terdiri dari satu atau lebih instruksi. Tiap instruksi dilaksanakan secara berurutan sesuai dengan urutan pelaksanaan, artinya suatu instruksi akan dilaksanakan setelah instruksi sebelumnya telah selesai dilaksanakan.
### Proses penyeleksian (selection)
Instruksi dikerjakan jika suatu kondisi tertentu dipenuhi. Dengan adanya proses ini maka ada kemungkinan beberapa jalur aksi yang berbeda berdasarkan kondisi yang ada.
### Proses pengulangan (looping)
Proses melakukan eksekusi suatu program secara berulang-ulang pada suatu blok instruksi tertentu yang terkendali.

### Outlines
    * Struktur Data Statis dan Dinamis
    * Struktur Data Linear dan Non Linear
    * Array
    * Structure
    * Pointers
    * Linked List

### Struktur Data Statis
Dalam struktur data Statis, ukuran struktur ditetapkan. Isi dari struktur data dapat dimodifikasi tetapi tanpa mengubah ruang memori yang dialokasikan padanya.

### Struktur Data Dinamis
Dalam struktur data dinamis, ukuran struktur tidak tetap dan dapat dimodifikasi selama operasi dilakukan di atasnya. Struktur data dinamis dirancang untuk memfasilitasi perubahan struktur data dalam runtime. Ukuran memori berubah tergantung perubahan data saat runtime

### Struktur Data Linear
1. Adalah Struktur data dimana elemen data disusun secara berurutan atau linier atau berurutan
2. Dalam struktur data linier, satu level dilibatkan. Oleh karena itu,proses hanya berupa proses tunggal. 
3. Struktur data linier mudah diimplementasikan karena memori komputer diatur secara linier.
4. Contoh :
    * Array
    * LinkedList
    * Stack
    * Queue

### Struktur Data Non Linear
1. Adalah Struktur data yang elemen datanya tidak tersusun secara berurutan atau linier. 
2. Struktur data non-linier tidak mudah diimplementasikan dibandingkan dengan struktur data linier. 
3. Menggunakan memori komputer secara efisien dibandingkan dengan struktur data linier. 
4. Contoh:
    * Tree
    * Graph

### Array
1. Array adalah kumpulan elemen-eleman data yang memiliki susunan tertentu dan teratur.
2. Jumlah elemen terbatas dan mempunyai tipe yang sama
3. Jenis Array
    * Array Satu Dimensi
    * Array Dua Dimensi
    * Array Tiga Dimensi

### Structure
Structure adalah koleksi berbagai variabel yang memiliki berbagai tipe data yang berbeda di dalam satu nama. 

### Pointers
Pointer adalah variabel yang menyimpan alamat memori sebagai nilainya.

Variabel pointer menunjuk ke tipe data (seperti int atau string) dari tipe yang sama, dan dibuat dengan operator *. 

### Linked List
* Struktur data linked list mencakup serangkaian node yang terhubung. Setiap node menyimpan data dan alamat node berikutnya.
* Setiap node struct memiliki item data dan penunjuk ke node struct lain. Harus ada alokasi memori untuk setiap struct.
* Linked List operations : Traverse, Insert, Delete


## Notasi Algoritma
1. Notasi algoritma bukan merupakan notasi bahasa pemrograman, namun notasi ini dapat diterjemahkan ke dalam berbagai bahasa pemrograman.
2. Meskipun notasi algoritma tidakberbentuk baku seperti notasi bahasa pemrograman, namun konsistensi terhadap notasi perlu diperhatikan untuk menghindari terjadinya kekeliruan.
3. Bentuk notasi algoritma:
    * Uraian deskriptif
    * Diagram-alir (flowchart)
    * Pseudocode

## Evaluasi
Untuk mengevalusi pemahaman tentang algoritma, berikut diberikan
beberapa pertanyaan dan pernyataan sebagai berikut;
1. Algorima dapat ditulis dengan sembarang bahasa? [B/S]
2. Urutan langkah dalam algorima boleh dibolak-balik? [B/S]
3. Algoritma boleh tidak memiliki output [B/S]
4. Algoritma boleh tidak memiliki input [B/S]
5. Algoritma boleh memiliki banyak input & sedikit outputnya [B/S]
6. Algoritma boleh memiliki sedikit input & banyak outputnya [B/S]
7. Algoritma boleh melakukan perulangan sampai tak terhingga [B/S]
8. Algoritma bercabang, cabangnya boleh berhenti [B/S]
9. Struktur while berhenti jika kondisinya benar [B/S]
10. Struktur repeat berhenti jika kondisinya benar [B/S]