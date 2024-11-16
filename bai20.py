#bai20.py: Nhap so nguyen a:
#Cho biet cac so nguyen to nho hon a
#Cho biet so luong cac so nguyen to nho hon a
#Tinh tong cac so nguyen to nho hon a

#Nhap so nguyen a
a = int(input("Nhap vao mot so nguyen: "))

#Khoi tao bien count va sum
count = 0
sum = 0
#Chay vong lap cac so trong khoang [2, a] (Note: Bo 1 vi 1 khong phai la so nguyen to)
if(a <= 2):
   print("Khong co so nguyen to nho hon", a)
else:
    print("Cac so nguyen to nho hon " + str(a) + " la:")
    for i in range(2, a):
        #Chay vong lap II kiem tra xem i co phai so nguyen to hay khong
        prime = True #Khoi tao bien prime
        for j in range(2, i):
            if(i % j == 0):
                prime = False
                break
        if prime:
            print(i)    
            count += 1
            sum += i
    print("Co " + str(count) + " so nguyen to be hon " + str(a))   
    print("Tong cac so nguyen to be hon " + str(a) + " = " + str(sum)) 