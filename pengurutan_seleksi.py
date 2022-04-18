

from ast import alias
"""
    Selection sort merupakan teknik sorting yang paling sederhana, hal pertama yang akan 
dilakukan algoritma selection sort adalah menemukan elemen terkecil dalam array kita dan 
menukarnya (swap) dengan elemen yang ada di posisi pertama, kemudian algoritma ini akan 
mengulangi hal yang sama lagi yaitu mencari elemen terkecil yang ada di dalam array dan 
kemudian menukarnya (swap) dengan elemen yang ada di posisi kedua (mengingat elemen di 
posisi pertama sudah berhasil kita sorting). Proses ini akan terus berlanjut sampai semua 
elemen yang ada di dalam array telah berhasil kita sorting.
"""

def selectionsort(alist):
    for i in range(0, len(alist)-1):
        minpositon = len(alist)-1
        for j in range(len(alist)-2, i-1, -1):
            if alist[j] < alist[minpositon]:
                minpositon = j
        temp = alist[i]
        alist[i] = alist[minpositon]
        alist[minpositon] = temp
        

# data
data = [9,7,10,8,12,11,14,13]
# menampilkan data sebelum diurutkan
print(data)

# memanggil fungsi selectionsort()
selectionsort(data)

# menampilkan data setelah diurutkan
print(data)