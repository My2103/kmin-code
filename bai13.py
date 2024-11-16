#bai13.py: Tinh tich cac uoc so chan cua so nguyn n

#Nhap vao mot so nguyen
n = int(input("Nhap mot so nguyen: "))

#Khoi tao bien tich
tich = 1

#Tim va tinh tich cac uoc so chan
for i in range (1, n+1):
    if(n % i == 0 and i % 2 == 0):
        tich *= i

#In ra ket qua
if(tich != 1):
    print("Tich cua cac uoc so chan =", tich)
else:
    print(n, "khong co uoc so chan")
