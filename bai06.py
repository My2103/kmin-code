#bai06.py: Cho nhập vào 3 số nguyên. Hãy đến các số âm

#Nhập vào 3 số nguyên
number1 = int(input("Nhập số nguyên I: "))
number2 = int(input("Nhập số nguyên II: "))
number3 = int(input("Nhập số nguyên III: "))

#Khởi tạo biến count
count = 0

#Kiểm tra, đếm số âm, và in ra kết quả
if(number1 < 0 or number2 < 0 or number3 < 0):
    if(number1 < 0):
        count += 1
    if(number2 < 0):
        count += 1
    if(number3 < 0):
        count += 1
    print("Có " + str(count) + " số âm.")
else:
    print("Bạn không nhập vào số âm nào cả.")