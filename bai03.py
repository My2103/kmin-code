#bai03.py: Tim ra gia tri so am dau tien trong mang

#Khai bao mang rong
a = []
n = int(input("Nhap vao so luong phan tu: "))

#Ham nhap mang
def nhap_mang():  
    for i in range(n):
        e = int(input(f"Nhap phan tu thu {i}: "))
        a.append(e)
    return a

#Ham tim so am dau tien
def tim_so_am(arr):
    for i in arr:
        if(i < 0):
            print("So am dau tien: ", i)
            break
    else:
        print("Khong co so am trong mang")

def cn_tim_so_am():
    array = nhap_mang()
    result = tim_so_am(array)

cn_tim_so_am()