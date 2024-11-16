#bai04.py: Nhap vao k, ve ra so ngoi sao = so k

#Nhap vao k
k = int(input("Nhap do dai doan thang: "))

#Khi bao bien S
s = ""

#Khai bao bien i
i = 1
#Tao vong lap
while i <= k:
    s += "* "
    i = i + 1

#In ket qua
print(s)

#Cach 2
#num = int(input("Nhap so luong: "))
num = 5
s = ""

while len(s) < num:
    s += "* "
print(s)