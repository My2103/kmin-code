#Bai05.py: Nhap vao n. In ra phep tinh S(n) = 1 + 1/2 + 1/3 +...+ 1/n

#Nhap vao mot so nguyen duong n
n = int(input("Nhap vao mot so nguyen duong: "))

#Kiem tra tinh hop le
while(n <= 0):
    print("Khong hop le. Vui long nhap mot so nguyen duong")
    n = int(input("Nhap vao mot so nguyen duong: "))

s = "1" #Tao mot bien chuoi

#Tao vong lap de tim ra cac so <= n
for i in range(2, n+1):
    s = str(s) + " + " + "1/" + str(i)

print("S(" + str(n) + ")" + " = " + str(s))