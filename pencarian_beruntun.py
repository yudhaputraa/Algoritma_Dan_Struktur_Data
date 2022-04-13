#
""" 
Algoritma Pencarian Bagi-Satu
Mengimplementasikan algoritma pencari beruntun(sequential search) 
atau pencarian lurus(linear search) di dalam python.

    Linear Search merupakan sebuah teknik pencarian data dengan menelusuri semua 
data satu per satu. Apabila ditemukan kecocokan data maka program akan mengembalikan 
output, jika tidak pencarian akan terus berlanjut hingga akhir dari array tersebut.

"""
#

## LINEAR SEARCH ##
def sequentialsearch(alist, value):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == value:
            found = True
        else:
            pos += 1
    if found:
        return pos
    else:
        return "Tdk ada"


data = [300,200,500,400,100]

# mencari nilai 400
sc1 = sequentialsearch(data, 400)
print("Hasil pencarian nilai sc1 :", sc1)
# mencari nilai 200
sc2 = sequentialsearch(data, 200)
print("Hasil pencarian nilai sc2 :", sc2)

# mencari nilai 700
sc3 = sequentialsearch(data, 700)
print("Hasil pencarian nilai sc3 :", sc3)

print("=="*14)
#
"""
Algoritma Pencarian Bagi-Dua
Mengimplementasikan algoritma pencari bagi-dua atau pencarian biner(binary search) di
dalam python.

    Binary Search merupakan sebuah teknik pencarian data dengancara berulang kali membagi 
separuh dari jumlah data yang dicari sampai sehingga memperkecil lokasi pencarian menjadi 
satu data. Dengan teknik ini kita akan membuang setengah dari jumlah data.
"""
#

def binarysearch(alist, value):
    first = 0
    last = len(alist) - 1
    found= False
    while first <= last and not found:
        middle = (first + last) // 2
        if alist[middle] == value:
            found = True
        else:
            if value < alist[middle]:
                last = middle -1
            else:
                first = middle + 1
    return found

data = [300,400,200,100,500]
print(data)
print("ini data yg belum di urutkan")

# mengurutkan data
data.sort()
print(data)
print("data ini sudah di urutkan")

# mencari nilai 200
print("mencari nilai 200 : ", binarysearch(data, 200))

# mencari nilai 500
print("mencari nilai 500 : ", binarysearch(data, 500))

# mencari nilai 700
print("mencari nilai 700 : ", binarysearch(data, 700))