#bai10.py: Tính BMI
import math
#Nhập vào số tuổi
tuoi = int(input("Nhập tuổi của bạn: "))


#Kiểm tra số tuổi
if tuoi < 18:
    print("Không khả dụng")
else:
    #Nhập vào chiều cao và cân nặng
    chieu_cao = float(input("nhập chiều cao của bạn (m): "))
    can_nang = float(input("Nhập cân nặng của bạn (kg): "))

    #Tính BMI
    BMI = can_nang / pow(chieu_cao, 2) #Có thể dùng 2 dấu sao (**) làm luỹ thừa

    #Trả kết quả BMI
    print("Chỉ số BMI của bạn:", BMI)
    #danh_gia = ""

    if BMI < 18.5:
        print("Gầy")
        #danh_gia = "Gay"
    elif 18.5 <= BMI < 25:
        print("Bình thường")
        #danh_gia = "Bình thường"
    elif 25 <= BMI < 30:
        print("Thừa cân")
    else:
        print("Béo phì")
    
    #print("danh_gia")