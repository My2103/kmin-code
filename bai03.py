#bai03.py: Cho nhap vao so nguyen duong n. Hay dem xem n co bao nhieu uoc so le

#Nhap vao mot so nguyen duong n
n = int(input("Nhap vao mot so nguyen duong: "))

#Kiem tra tinh hop le
while(n <= 0):
    print("Khong hop le. Vui long nhap mot so nguyen duong")
    n = int(input("Nhap vao mot so nguyen duong: "))

#Chay vong lap tim uoc so
count = 0 #Khai bao bien count dem uoc so
for i in range(1, n+1):
    if(n % i == 0) and (i % 2 != 0):
        print(i)
        count += 1

#In ra ket qua
print(str(n) + " co " + str(count) + " uoc so le.") 