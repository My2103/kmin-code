#bai02.py: giai phuong trinh bac nhat ax + b = 0 

#Nhap hai gia tri a và b
a = int(input("Nhap gia tri a: "))
b = int(input("Nhap gia tri b: "))

#Kiem tra nghiem cua phuong trinh
if(a == 0 and b != 0):
    print("Phuong trinh vo nghiem.")
elif(a == 0 and b == 0):
    print("Phuong trinh vo so nghiem.")
else:
    x = -b/a
    print("Nghiem cua phuong trinh:", x)
