#bai10.py: Dem so chan bang vong lap

#Nhap vao hai so nguyen
m = int(input("Nhap vao so m: "))
n = int(input("Nhap vao so n: "))

#Vong lap
dem = 0
for i in range(m, n+1):
    if i % 2 == 0:
        dem += 1
    
print(dem)