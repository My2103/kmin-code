#bai06.py: Cho phep nguoi dung nhap vao mot so nguyen nho hon 1000. 
#Chuong trinh se cho biet chu so hang don vi, hang chuc, hang tram

#Nguoi dung nhap vao mot chu so nho hon 1000
number = int(input("Nhap vao mot so: "))

#Kiem tra so co hop le hay khong
if(number > 1000):
    print("Khong hop le")

else:
    #Tinh hang don vi, chuc, tram
    don_vi = number%10
    chuc = (number/10)%10
    tram = number/100

    #In ra ket qua
    print("Don vi:", int(don_vi))
    print("Chuc:", int(chuc))
    print("Tram:", int(tram))


