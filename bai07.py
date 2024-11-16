#bai07.py: Hay cho biet trong mang co phai toan so am khong

#Khai bao mang rong
a = []
n = int(input("Nhap vao so luong phan tu: "))

#Ham nhap mang
def nhap_mang():
    for i in range(n):
        e = int(input(f"Nhap phan tu thu {i}: "))
        a.append(e)
    return a

#Ham tim so duong
def tim_so_duong(arr):
    find_positive = False
    for i in arr:
        if(i > 0):
            find_positive = True
    return find_positive

def cn_tim_so_duong():
    array = nhap_mang()
    result = tim_so_duong(array)
    if(result == False):
        print("Day la mang toan am")
    else:
        print("Day khong phai la mang toan am")

cn_tim_so_duong()