#
"""
mengimplementasikan algoritma pengurutan gelembung(bubble sort)
di dalam  bahasa python.

    Bubble Sort adalah metode pengurutan algoritma dengan cara melakukan 
penukaran data secara terus menerus sampai bisa dipastikan dalam suatu iterasi 
tertentu tidak ada lagi perubahan/penukaran
"""
#

def bubblesort(alist):
    for i in range(0, len(alist)-1):
        for j in range(len(alist)-1, i, -1):
            if alist[j] < alist[j-1]:
                temp = alist[j]
                alist[j] = alist[j-1]
                alist[j-1] = temp

data = [9,7,10,8,12,11,14,13]
print("menampilkan data sebelum diurutkan")
print(data)

# memanggil fungsi bubblesort()
bubblesort(data)

print("menampilkan data setelah diurutankan")
print(data)
