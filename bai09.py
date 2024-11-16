#Nhập vào một tháng trong năm nay. Hãy cho biết tháng đó có bao nhiêu ngày

#Nhập vào một tháng
thang = int(input("Nhập vào một tháng: "))

#Kiểm tra tháng đó có bao nhiêu ngày và in ra kết quả
if(thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12):
    print("Tháng này có 31 ngày.")
elif(thang == 4 or thang == 6 or thang == 9 or thang == 11):
    print("Tháng này có 30 ngày.")
else:
    print("Tháng này có 29 trong năm nay (2024).")

#cách 2
#so_ngay = None
#if(thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12):
    #so_ngay = 31
#elif(thang == 4 or thang == 6 or thang == 9 or thang == 11):
    #so_ngay = 30
#else:
    #so_ngay = 29

#print(so_ngay)

#Cách 3
#if thang in [1, 3, 5, 7, 8, 10, 12]:
    #so_ngay = 31