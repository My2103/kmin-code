#bai04.py: Ham goi ham

def xin_chao(ten, nam_sinh):
    print(f"Xin chao, minh ten la {ten}.")
    print(f"Minh sinh nam {nam_sinh}.")
    print("Rat vui duoc gap ban.")
    tuoi = 2024 - nam_sinh
    return tuoi

def cn_xin_chao():
    name = input("Nhap ten: ")
    yob = int(input("Nhap nam sinh: "))
    print()
    t = xin_chao(name, yob)
    print("Minh " + str(t) + " tuoi.")

cn_xin_chao()