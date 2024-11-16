""""
#bai15.py: Cho uoc so nguyen n, voi n > 1. Hay cho biet so nguyen n cos uoc so trong doan [2, n- 1] khong

#Nhap so nguyen n
n = int(input("Nhap so nguyen n: "))


#Kiem tra tinh hop le
if(n < 1):
    print("Khong hop le. Vui long nhap so lon hon 1.")
else:
    #Kiem tra n co uoc so trong khoang [2, n-1] khong
    #print("Uoc so cua " + str(n) + " trong khoang tu 2 den " + str(n-1) + " la:")
    found = False #biến cờ để theo dõi
    for i in range(2, n):
        if(n%i == 0):
            found = True
            break

if found == True:
    print("Yes")
else:
    print("No")
"""
#Viet theo kieu ham
"""
def co_uoc(n):
    found = False
    for i in range(2, n):
        if(n%i == 0):
            found = True
            break
    return found
"""
#Cách khác:
def co_uoc_2(n):
    for i in range(2, n):
        if n % i == 0:
            return True
    return False

def cn_co_uoc():
    n = int(input("Nhap so nguyen n: "))
    if co_uoc_2(n) == True:
        print("Yes")
    else:
        print("No")

cn_co_uoc()
