#bai07.py: Tinh so nut bien so xe

#Nhap vao 1 so nguyen gom 5 chu so
number = int(input("Nhap vao mot so: "))

#Kiem tra tinh hop le
if(number < 0):
    print("Khong hop le")

else:
    number_digit1 = number/10000
    number_digit2 = (number/1000)%10
    number_digit3 = (number/100)%10
    number_digit4 = (number/10)%10
    number_digit5 = number%10

    sum = number_digit1 + number_digit2 + number_digit3 + number_digit4 + number_digit5

    sum_digit1 = sum/10
    sum_digit2 = sum%10

    so_nut = sum_digit1 + sum_digit2

    print("So nut:", so_nut)

