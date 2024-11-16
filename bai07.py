#bai07.py: Tam giac deu

#Ham kiem tra tam giac deu
def tam_giac_deu(x, y, z):
    if(x == y == z):
        return True
    else:
        return False
    
def cn_tam_giac_deu():
    a = int(input("Nhap a: "))
    b = int(input("Nhap b: "))
    c = int(input("Nhap c: "))

    result = tam_giac_deu(a, b, c)

    if(result == True):
        print("Day la tam giac deu.")
    else:
        print("Day khong phai la tam giac deu.")

cn_tam_giac_deu()