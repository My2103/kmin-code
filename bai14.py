#bai14.py: Tim so dau tien chia het cho 6 trong doan [m, n]. Luu y: duyet tu m den n

#Nhap m, n
m = int(input("Nhap m: "))
n = int(input("Nhap n: "))

#Kiem tra tinh hop le
if(m > n):
    print("Khong hop le, vui long nhap m be hon n.")
else:
    #Chay vong lap for tim ra so chia het cho 6 trong khoang [m, n]
    for i in range(m, n+1):
        if(i % 6 == 0):
            print("So dau tien chi het cho 6 trong khoang tu " + str(m) + " den " + str(n) + " la " + str(i))
            break
    else:
        print("Khong co so chia het cho 6 trong khoang tu " + str(m) + " den " + str(n))

def tim(m, n):
    for i in range(m, n+1):
        if(i % 6 == 0):
            return i
    else:
        return "Khong co"

def cn_tim():
    m = int(input("Nhap m: "))
    n = int(input("Nhap n: "))
    kq = tim(m, n)
    print(kq)

cn_tim()    