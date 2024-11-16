#bai04.py: Cho mot mang luu cac ma so sinh vien. 
#Cho phep nhap vao mot ma so. Hay cho biet ma so nay xuat hien o dau trong mang

#Khai bao mang rong
a = []
n = int(input("Nhap vao so luong phan tu: "))

#Ham nhap mang
def nhap_mang():  
    for i in range(n):
        e = int(input(f"Nhap phan tu thu {i}: "))
        a.append(e)
    return a

#Ham tim so
def tim_so(arr):
    number = int(input("Nhap so ban can tim: "))

    for i in range(len(arr)):
        if(number == arr[i]):
            print("So ban can tim o vi tri so", i)

def cn_tim_so():
    array = nhap_mang()
    tim_so(array)

cn_tim_so()