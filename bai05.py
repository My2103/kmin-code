#bai05.py: Tim so lon nhat trong mang

#Khai bao mang rong
a = []
n = int(input("Nhap vao so luong phan tu: "))

#Ham nhap mang
def nhap_mang():  
    for i in range(n):
        e = int(input(f"Nhap phan tu thu {i}: "))
        a.append(e)
    return a

#Ham tim so lon nhat
def tim_so_lon_nhat(arr):
    max = arr[0]

    for i in range(len(arr)):
        if(arr[i] > max):
            max = arr[i]

    return max

def cn_tim_so_lon_nhat():
    array = nhap_mang()
    result = tim_so_lon_nhat(array)
    print("So lon nhat trong mang la:", result)

cn_tim_so_lon_nhat()