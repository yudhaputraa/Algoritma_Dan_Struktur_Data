"""
    Insertion Sort merupakan sebuah teknik pengurutan dengan cara membandingkan dan 
mengurutkan dua data pertama pada array, kemudian membandingkan data para array berikutnya 
apakah sudah berada di tempat semestinya. Algorithma insertion sort seperti proses pengurutan 
kartu yang berada di tangan kita.
"""

def insertionsort(alist):
    for i in range(1, len(alist)):
        currentvalue = alist[i]
        position = i 
        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position -= 1
        alist[position] = currentvalue

data = [12,10,6,11,5,4,7,9,8]
# menampilkan data sebelum diurutkan
print(data)

# memanggil fungsi insertionsort()
insertionsort(data)

# menampilkan data setelah diurutkan
print(data)

"""
Penjelasan
    Pada algoritma pengurutan sisipan, program akan menyisipkan suatu
elemen list pada posisi yang sesuai. Posisi tersebut dicari dengan cara
membandingkan suatu elemen dengan elemen-elemen sebelumnya
Pada algoritma ini, mula-mula elemen pertama dianggap telah berada
pada posisi yang tepat. Selanjutnya, elemen kedua akan dibandingkan
dengan elemen pertama. Jika elemen pertama lebih besar dari elemen
kedua, maka elemen pertama akan digeser ke kanan menjadi elemen
kedua dan elemen kedua sebelumnya akan disisipkan pada posisi
pertama. Setelah itu, elemen ketiga akan dibandingkan dengan elemen
kedua dan pertama. Jika elemen kedua lebih besar dari elemen ketiga,
maka elemen kedua akan digeser ke kanan. Selanjutnya, elemen ketiga
akan dibandingkan lagi dengan elemen pertama. Jika elemen pertama
lebih besar dari elemen ketiga, maka elemen pertama juga akan digeser
ke kanan dan elemen ketiga akan disisipkan pada posisi pertama. Jika
elemen pertama lebih kecil dari elemen ketiga, maka elemen ketiga akan
disisipkan pada posisi kedua. Demikian seterusnya sampai semua
elemen di dalam list diproses.
"""