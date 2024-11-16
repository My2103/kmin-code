#bai09.py: Kiem tra so nguyen to

#Ham kiem tra so nguyen to
def so_nguyen_to(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def cn_so_nguyen_to():
    number = int(input("Nhap vao mot so: "))
    result = so_nguyen_to(number)

    if(result == True):
        print("Day la so nguyen to.")
    else:
        print("Day khong phai la so nguyen to.")

cn_so_nguyen_to()