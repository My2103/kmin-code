#bai07.py: Nhập vào 3 số nguyên. Hãy tính tổng các số âm

#Nhập vào 3 số nguyên
number1 = int(input("Nhập số nguyên I: "))
number2 = int(input("Nhập số nguyên II: "))
number3 = int(input("Nhập số nguyên III: "))

#Khởi tạo biến sum
sum = 0

#Kiểm tra số âm và tính tổng
if(number1 < 0 or number2 < 0 or number3 < 0):
    if(number1 < 0):
        sum += number1
    if(number2 < 0):
        sum += number2
    if(number3 < 0):
        sum += number3
    print("Tổng các số âm =", sum)
else:
    print("Bạn không nhập vào số âm nào cả.")