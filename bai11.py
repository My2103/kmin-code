#bai11.py: Dem so luong uoc cua so nguyen n

#Nhap vao mot so nguyen
n = int(input("Nhap vao mot so: "))

#Khoi tao bien dem
dem = 0

#Khoi tao vong lap
for i in range(1, n+1):
    if n % i == 0:
        dem += 1

#In ra ket qua
print("So uoc cua " + str(n) + " la " + str(dem))