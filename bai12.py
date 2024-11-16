#bai12.py: Tinh tong cac so nguyen trong khoang [1, n]

#Nhap vao mot so nguyen
n = int(input("Nhap vao mot so: "))

i = 1 #Khoi tao bien i = 1
sum = 0 #Khoi tao bien sum = 0

#Cach 1: Dung vong lap while
#Tim ra cac so nguyen trong khoang [1, n]
while(i <= n):
    sum += i
    i = i + 1

#In ra ket qua
print("Tong cac so nguyen trong khoang [1, n]:", sum)

