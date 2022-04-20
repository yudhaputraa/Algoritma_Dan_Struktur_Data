"""
    Shell Sort adalah salah algoritma dalam melakukan sorting, atau pengurutan data Angka. 
Tekniknya, dengan melakukan perbandingan angka pada 2 posisi dengan jarak tertentu, jarak 
disini diartikan jarak posisi antara 2 bilangan yang ingin dibandingkan.
"""

# fungsi pengurutan sisipan yg di modifikasi
def insertionsort(alist, start, step):
    for i in range(start+step, len(alist), step):
        currentvalue = alist[i]
        position = i
        while position >= step and alist[position-step] > currentvalue:
            alist[position] =  alist[position-step]
            position -= step
            alist[position] = currentvalue

# algoritma pengurutan shell
def shellsort(alist):
    step = len(alist) // 2
    while step > 0:
        for i in range(step):
            # memangil fungsi insertionsort()
            insertionsort(alist, i, step)
        step = step // 2

data = [12,10,6,11,5,4,7,9,8]

# menampilkan data sebelum di urutkan
print(data)

# memanggil metode shellsort()
shellsort(data)

# menampilkan data setelah di urutkan
print(data)

"""
Penjelasan
    Nama algoritma pengurutan Shell diambil dari nama penemunyaDonald Shell. Algoritma ini merupakan bentuk penyederhanaan algoritma pengurutan sisipan. Dengan demikian, pada dasarnya
pengurutan Shell juga menggunakan algoritma pengurutan sisipanNamun, dalam algoritma pengurutan Shell, elemen-elemen list dibagi
menjadi beberapa sub-list. Selanjutnya, setiap sub-list tersebut
diurutkan menggunakan algoritma sisipan. Hal ini bertujuan untuk
mengurangi banyaknya proses pergeseran elemen yang terjadi di dalam
algoritma pengurutan sisipan.
"""