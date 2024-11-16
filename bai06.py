#bai06.py: Hay cho biet trong mang co ton tai so am khong

#Khai bao mang rong
a = []
n = int(input("Nhap vao so luong phan tu: "))

#Ham nhap mang
def nhap_mang():  
    for i in range(n):
        e = int(input(f"Nhap phan tu thu {i}: "))
        a.append(e)
    return a

#Ham tim so am
def tim_so_am(arr):
    find_negative = False
    for i in arr:
        if i < 0:
            find_negative = True
    return find_negative

def cn_tim_so_am():
    array = nhap_mang()
    result = tim_so_am(array)
    print(result)

cn_tim_so_am()