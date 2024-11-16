#bai05.py: Cho nhập vào 3 số nguyên hãy in ra màn hình các số âm

#Người dùng nhập vào 3 số nguyên
number1 = int(input("Nhập số nguyên I: "))
number2 = int(input("Nhập số nguyên II: "))
number3 = int(input("Nhập số nguyên III: "))

#Kiểm tra và in ra các số âm
if(number1 < 0 or number2 < 0 or number3 < 0):
    print("Các số âm là: ")
    if(number1 < 0):
        print(number1)
    if(number2 < 0):
        print(number2)
    if(number3 < 0):
        print(number3)
else:
    print("Bạn không nhập vào số âm nào cả.")
    