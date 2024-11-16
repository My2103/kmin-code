#bai02.py: Kiểm tra tam giác này có phẩi tam giác đều hay không

#Promt 3 egde of triangle from user
a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))

#Check
#if (a == b and b == c):
    #print("Đây là tam giác đều.")
#else:
    #print("Đây không phải là tam giác đều.")

#if not(a == b and b == c):
    #print("Đây là tam giác đều.")
#else:
    #print("Đây không phải là tam giác đều.")

# De Morgan
#not (A and B)
#not(A) or not(B)

if not(a == b and b == c):
    print("Đây là tam giác không đều.")
else:
    print("Đây là tam giác đều.")
