#bai04.py: Phân loại sinh viên

#Người dùng nhập vào số điểm
diem = float(input("Nhập điểm của bạn: "))

#Xét sinh viên có đủ điều kiện tốt nghiệp hay không và cho biết loại xếp hạng (nếu có)
if(diem < 5.0):
    print("Bạn không đủ điều kiện tốt nghiệp.")
else:
    print("Bạn đủ điều kiện tốt nghiệp.")
    if(diem >= 8.0):
        print("Loại giỏi.")
    elif(diem >= 6.5):
        print("Loại khá.")
    else:
        print("Loại trung bình.")