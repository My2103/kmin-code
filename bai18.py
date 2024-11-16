#bai18.py: In hinh chu nhat rong

#Nhap vao w va h
w = int(input("Nhap w: "))
h = int(input("Nhap h: "))

#Vong lap in ra hinh chu nhat rong
for i in range(h):
    for j in range(w):
        if i == 0 or i == h-1 or j == 0 or j == w-1:
            print("* ", end="")
        else:
            print("  ", end = "")
    print()
    