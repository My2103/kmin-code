#Bai04.py: Cho phep nhap vao mot so nguyen duong n. Hay tinh tich cac uoc so cua n

#Nhap vao mot so nguyen duong n
n = int(input("Nhap vao mot so nguyen duong: "))

#Kiem tra tinh hop le
while(n <= 0):
    print("Khong hop le. Vui long nhap mot so nguyen duong")
    n = int(input("Nhap vao mot so nguyen duong: "))

#Tao vong lap tim uoc so
multiple = 1 #Khoi tao bien multiple de nhan cac uoc so

for i in range(2, n+1):
    if(n % i == 0):
        multiple *= i

print("Tich cua cac uoc so:", multiple)
