#bai02.py: Nhap vao mot mang so nguyen

#Khai bao mang rong
a = []
n = int(input("Nhap vao so luong phan tu: "))

#Ham nhap mang
def nhap_mang():  
    for i in range(n):
        e = int(input(f"Nhap phan tu thu {i}: "))
        a.append(e)
    return a

def test_nhap_mang():
    b = nhap_mang()
    print(b)

#Ham liet ke so duong
def liet_ke_so_duong(arr):
    print("Phan tu duong la: ")
    for e in arr:
        if e > 0:
            print(i)

#Ham test liet ke duong
def test_lk_duong():
    a = nhap_mang()
    liet_ke_so_duong(a)

#Ham dem so le
def dem_so_le(arr):
    count = 0
    for i in arr:
        if(i % 2 != 0):
            count += 1
    return count

def test_dem_so_le():
    array = nhap_mang()
    kq = dem_so_le(array)
    print(f"Co {kq} so le trong mang.")

#Ham tinh tong cac so am trong mang
def cong_so_am(arr):
    sum = 0
    for i in arr:
        if(i < 0):
            sum += i
    return sum

def test_cong_so_am():
    array = nhap_mang()
    sum = cong_so_am(array)
    print("Tong cac so am trong mang =", sum)


test_cong_so_am()

