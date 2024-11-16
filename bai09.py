#bai09.py: Nhap so nguyen n. In ra uoc so

#Nhap vao mot so nguyen
n = int(input("Nhap vao mot so: "))

#for i in range(1, n+1):
    #if n % i == 0:
        #print(i) 

i = 1

while i <= n:
    if n % i == 0:
        print(i) 
    i = i + 1
