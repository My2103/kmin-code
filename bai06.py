#bai06.py: Doi nhiet do

#Ham doi nhiet do
def doi_nhiet_do(F):
    C = 5/9 * (F - 32)
    return C

def cn_doi_nhiet_do():
    F = int(input("Nhap do F: "))
    C = doi_nhiet_do(F)
    print("Do C =", C)

cn_doi_nhiet_do()