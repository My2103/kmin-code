#bai01.py: Cho nhap vao so nguyen duong n. 
#Hay in ra man hinh n chuoi co dang nhu sau: "Kmin 1", "Kmin 2", "Kmin n"

#Nhap vao mot so nguyen duong n
n = int(input("Nhap vao mot so nguyen duong: "))

#Kiem tra tinh hop le
while(n <= 0):
    print("Khong hop le. Vui long nhap mot so nguyen duong")
    n = int(input("Nhap vao mot so nguyen duong: "))

#Tao vong lap, in ra chuoi
i = 1 #Khoi tao bien i = 1

while(i <= n):
    print("Kmin " + str(i))
    i = i + 1
