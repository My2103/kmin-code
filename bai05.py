
def xin_chao(ten, nam_sinh):
    print(f"Xin chao, minh ten la {ten}.")
    print(f"Minh sinh nam {nam_sinh}.")
    print("Rat vui duoc gap ban.")
    tuoi = 2024 - nam_sinh
    return tuoi
    
def nhap_nam_sinh():
    yob = int(input("Nhap nam sinh: "))
    while (yob < 1900 or yob >= 2024):
        print("Khong hop le. Vui long nhap lai.")
        yob = int(input("Nhap nam sinh: "))
    return yob

def nhap_ten():
    name = input("Nhap ten: ")
    while(name == ""):
        print("Vui long nhap ten cua ban.")
        name = input("Nhap ten: ")
    return name

def cn_xin_chao():
    name = nhap_ten()
    yob = nhap_nam_sinh()
    print()
    t = xin_chao(name, yob)
    print("Minh " + str(t) + " tuoi.")

cn_xin_chao()