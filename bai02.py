#bai02.py: Cho phep nhap vào mot so nguyen duong n. Hay in ra man hinh cac uoc so chan cua so nguyen n

#Nhap vao mot so nguyen duong n
n = int(input("Nhap vao mot so nguyen duong: "))

#Kiem tra tinh hop le
while(n <= 0):
    print("Khong hop le. Vui long nhap mot so nguyen duong")
    n = int(input("Nhap vao mot so nguyen duong: "))

#Chay vong lap for de tim uoc so cua n
even = False
print("Cac uoc so chan cua " + str(n) + " la: ")
for i in range(2, n+1):
    if (n % i == 0) and (i % 2 == 0):
        print(i)
        even = True

#In ra ket qua
if not even:
    print("Khong co")