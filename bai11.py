#bai11.py: Cho phép nhập vào một ngày gồm ngày, tháng, năm. Hãy cho biết ngày này có hợp lệ không.

#Nhập ngày, tháng, năm
ngay = int(input("Ngày: "))
thang = int(input("Thang: "))
nam = int(input("Năm: "))

#Kiểm tra tính hợp lệ

if(1 <= thang <= 12 and nam > 0):
    if(thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12):
        if(0 < ngay <= 31):
            print("Hợp lệ.")
        else:
            print("Không hợp lệ.")
    if(thang == 4 or thang == 6 or thang == 9 or thang == 11):
        if(0 < ngay <= 30):
            print("Hợp lệ")
        else:
            print("Không hợp lệ")
    if(thang == 2):
        if(nam%4==0 and nam%100!=0) or (nam%400==0):
            if(0 < ngay <= 29):
                print("Hợp lệ")
            else:
                print("Không hợp lệ")
        else:
            if(0 < ngay <= 28):
                print("Hợp lệ")
            else:
                print("Không hợp lệ")
else:
    print("Không hợp lệ")
