import math

#Nhap vao toa do hai diem
a1 = int(input("Nhap toa do a1: "))
a2 = int(input("Nhap toa do a2: "))

b1 = int(input("Nhap toa do b1: "))
b2 = int(input("Nhap toa do b2: "))

#Tinh khoang cach hai diem A va B
AB = math.sqrt(pow((b1 - a1), 2) + pow((b2 - a2), 2))

#In ket qua
print("Khoang cach giua 2 diem:", AB)