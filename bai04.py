#bai04.py: Tinh tien

#Nhap so luong va don gia
sl = float(input("Nhap so luong: "))
donGia = float(input("Nhap don gia: "))

#Tinh tien thuc te phai tra
tien = sl * donGia

#Tinh thue gia tri gia tang
thue_gia_tri_gia_tang = (10/100) * tien

#Tinh tong tien
tong = tien + thue_gia_tri_gia_tang

#In ket qua
print("Tien =", tien)
print("Thue gia tri gia tang =", thue_gia_tri_gia_tang)
print("Tong =", tong)
