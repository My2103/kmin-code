#bai08.py: a so voi b

#Ham a so voi b
def so_sanh(a, b):
    if a > b:
        print("Lon")
    elif a < b:
        print("Nho")
    else:
        print("Bang")

def cn_so_sanh():
    a = int(input('Nhap a: '))
    b = int(input('Nhap b: '))

    result = so_sanh(a, b)

cn_so_sanh()