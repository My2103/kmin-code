"""
#bai16.py: Nhap vao so nguyen va tim so nguyen to

#Nhap vao so n
n = int(input("Nhap vao n: "))

#Kiem tra so nguyen to
prime = True #Khoi tao bien co prime

if(n <= 1):
    prime = False

for i in range(2, n):
    if(n % i == 0):
        prime = False
    
if not prime:
    print(str(n) + " khong phai la so nguyen to.")
else:
    print(str(n) + " la so nguyen to.")
"""

def la_snt_2(n):
    if (n < 2):
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(la_snt_2(16))
