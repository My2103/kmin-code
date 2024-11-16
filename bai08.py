#bai08.py: Nhap vao so k, in ra *$
#Nhap vao mot so nguyen
k = int(input("Nhap vao mot so: "))

s = ""
for i in range(k):
    if(i % 2 == 0):
        s += "* "
    else:
        s += "$ "
print(s)

