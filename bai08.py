#bai08.py: Nhập vào một năm. Kiểm tra năm đó có phải là năm nhuận hay không

#Nhập vào một năm
nam = int(input("Nhập năm vào đây: "))

#Kiểm tra năm đó có phải là năm nhuận hay không
if(nam%4==0 and nam%100!=0) or (nam%400==0):
    print(str(nam) + " là năm nhuận.")
else:
    print(str(nam) + " không phải là năm nhuận.")