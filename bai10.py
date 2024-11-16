#bai10.py: Liet ke cac so nguyen to

#Ham kiem tra so nguyen to
def so_nguyen_to(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def liet_ke_snt():
    m = int(input("Nhap vao mot so: "))
    n = int(input("Nhap vao mot so: "))

    while (m > n):
        print("\nKhong hop le")
        m = int(input("Nhap vao mot so: "))
        n = int(input("Nhap vao mot so: "))

    for i in range(m , n+1):
        result = so_nguyen_to(i)
        if (result == True):
            print(i)

liet_ke_snt()
