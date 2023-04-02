# Linked list

Linked list adalah struktur data dinamis yang terdiri dari serangkaian simpul (node) yang saling terhubung. Setiap simpul dalam linked list terdiri dari dua komponen, yaitu data dan pointer yang menunjukkan simpul berikutnya dalam linked list.

Algoritma untuk membuat linked list biasanya terdiri dari langkah-langkah berikut:
* Inisialisasi pointer head sebagai NULL.
* Buat sebuah simpul baru dengan alokasi memori dinamis.
* Masukkan data ke dalam simpul baru tersebut.
* Buat simpul baru menunjuk ke simpul yang sebelumnya dengan mengatur pointer dari simpul sebelumnya ke simpul baru.
* Atur pointer head menunjuk ke simpul pertama dalam linked list.

Algoritma untuk menambahkan simpul baru ke akhir linked list terdiri dari langkah-langkah berikut:
* Jika linked list kosong, maka buat simpul baru dan atur pointer head untuk menunjuk ke simpul tersebut.
* Jika linked list tidak kosong, cari simpul terakhir dalam linked list.
* Buat simpul baru dan atur simpul terakhir dalam linked list menunjuk ke simpul baru.

Algoritma untuk menghapus simpul dari linked list terdiri dari langkah-langkah berikut:
* Cari simpul yang akan dihapus.
* Jika simpul yang akan dihapus adalah simpul pertama dalam linked list, atur pointer head untuk menunjuk ke simpul berikutnya.
* Jika simpul yang akan dihapus bukan simpul pertama dalam linked list, atur pointer dari simpul sebelum simpul yang akan dihapus untuk menunjuk ke simpul setelah simpul yang akan dihapus.
* Hapus simpul yang diinginkan dari memori.

Algoritma untuk mencetak isi linked list terdiri dari langkah-langkah berikut:
* Mulai dari simpul pertama dalam linked list.
* Cetak data dari simpul tersebut.
* Pindah ke simpul berikutnya dalam linked list.
* Ulangi langkah 2-3 sampai semua simpul dalam linked list telah dicetak.

Pada umumnya, algoritma untuk linked list akan selalu melibatkan pointer untuk menunjuk ke simpul lain dalam linked list. Oleh karena itu, pemahaman yang kuat tentang konsep pointer dalam pemrograman sangat penting untuk menguasai algoritma linked list dengan baik.

Beberapa algoritma umum lainnya yang berkaitan dengan linked list antara lain:

Algoritma untuk menghitung jumlah simpul dalam linked list
Mulai dari simpul pertama dalam linked list
Ulangi langkah berikutnya untuk setiap simpul dalam linked list: tambahkan 1 ke hitungan
Kembalikan hitungan
Algoritma untuk mencari simpul tertentu dalam linked list
Mulai dari simpul pertama dalam linked list
Ulangi langkah berikutnya untuk setiap simpul dalam linked list: periksa apakah data simpul saat ini sama dengan data yang dicari
Jika data ditemukan, kembalikan simpul tersebut, jika tidak, kembalikan NULL
Algoritma untuk membalik linked list
Inisialisasi tiga pointer: prev, curr, dan next
Atur pointer curr menunjuk ke simpul pertama dalam linked list, dan atur pointer prev dan next menjadi NULL
Ulangi langkah berikutnya untuk setiap simpul dalam linked list:
a. Atur pointer next untuk menunjuk ke simpul berikutnya dalam linked list
b. Atur pointer curr untuk menunjuk ke simpul sebelumnya dalam linked list
c. Atur pointer prev untuk menunjuk ke simpul saat ini
d. Pindahkan pointer curr dan next ke simpul berikutnya dalam linked list
Atur pointer head untuk menunjuk ke simpul terakhir dalam linked list (simpul yang sebelumnya menjadi simpul terakhir setelah dibalik)
Algoritma untuk menggabungkan dua linked list
Buat linked list baru
Mulai dari simpul pertama dalam linked list pertama
Ulangi langkah berikutnya untuk setiap simpul dalam linked list pertama: buat simpul baru dan masukkan data dari simpul saat ini, lalu tambahkan simpul baru ke linked list baru
Mulai dari simpul pertama dalam linked list kedua
Ulangi langkah berikutnya untuk setiap simpul dalam linked list kedua: buat simpul baru dan masukkan data dari simpul saat ini, lalu tambahkan simpul baru ke linked list baru
Kembalikan linked list baru yang berisi kedua linked list yang digabungkan
Itulah beberapa algoritma umum yang berkaitan dengan linked list. Dalam pemrograman, linked list sering digunakan untuk menyimpan dan mengelola data yang terhubung secara dinamis, seperti dalam aplikasi pengolah kata, program permainan, dan sistem manajemen database. Memahami algoritma linked list dan konsep pemrograman yang terkait dapat membantu kamu menjadi seorang programmer yang lebih terampil dan efektif.

Selain algoritma-algoritma yang telah dijelaskan sebelumnya, ada juga beberapa operasi umum yang sering dilakukan pada linked list, yaitu:

Menambahkan simpul di awal linked list (insertion at the beginning)
Buat simpul baru dan masukkan data ke dalamnya
Atur pointer simpul baru untuk menunjuk ke simpul pertama dalam linked list
Atur pointer head untuk menunjuk ke simpul baru
Menambahkan simpul di akhir linked list (insertion at the end)
Buat simpul baru dan masukkan data ke dalamnya
Mulai dari simpul pertama dalam linked list
Ulangi langkah berikutnya untuk setiap simpul dalam linked list: pindahkan pointer ke simpul berikutnya sampai pointer menunjuk ke NULL
Atur pointer simpul terakhir untuk menunjuk ke simpul baru
Menambahkan simpul pada posisi tertentu dalam linked list (insertion at a specific position)
Buat simpul baru dan masukkan data ke dalamnya
Mulai dari simpul pertama dalam linked list
Ulangi langkah berikutnya untuk setiap simpul dalam linked list: pindahkan pointer ke simpul berikutnya sampai mencapai posisi yang diinginkan
Atur pointer simpul baru untuk menunjuk ke simpul pada posisi berikutnya
Atur pointer simpul pada posisi sebelumnya untuk menunjuk ke simpul baru
Menghapus simpul dari linked list
Mulai dari simpul pertama dalam linked list
Ulangi langkah berikutnya untuk setiap simpul dalam linked list: periksa apakah data simpul saat ini sama dengan data yang ingin dihapus
Jika data ditemukan, atur pointer simpul sebelumnya untuk menunjuk ke simpul berikutnya (atau NULL jika simpul dihapus adalah simpul pertama)
Jika data tidak ditemukan, kembalikan pesan error
Dengan memahami operasi-operasi ini dan algoritma-algoritma terkait, kamu dapat membuat program yang efektif dan efisien untuk mengelola linked list. Selain itu, kamu juga dapat mempelajari berbagai struktur data lainnya yang dapat digunakan untuk menyimpan dan mengelola data dalam aplikasi pemrograman.