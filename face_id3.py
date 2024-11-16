import face_recognition

#Nhap file anh A va ten cua nguoi trong anh A
image_A_path = 'IMG_A.JPG'
name_A = "MyMy"

#Nhap file anh B
image_B_path = 'IMG_B.JPG'

#Doc anh tu file
image_A = face_recognition.load_image_file(image_A_path)
image_B = face_recognition.load_image_file(image_B_path)

# Mã hóa khuôn mặt trong ảnh A
face_encoding_A = face_recognition.face_encodings(image_A)[0]

# Mã hóa khuôn mặt trong ảnh B
face_encodings_B = face_recognition.face_encodings(image_B)

# So sánh khuôn mặt trong ảnh B với khuôn mặt trong ảnh A
results = face_recognition.compare_faces(face_encodings_B, face_encoding_A)

# Kiểm tra kết quả và in ra thông báo
if True in results:
    print(f"Người trong ảnh B là {name_A}.")
else:
    print("Người trong ảnh B không phải là người trong ảnh A.")