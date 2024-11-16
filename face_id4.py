import face_recognition
import cv2

# Nhập tên file ảnh A và tên của người trong ảnh A
image_A_path = 'IMG_A.JPG'
name_A = "MyMy"

# Nhập tên file ảnh B
image_B_path = 'face_image.png'

# Đọc ảnh từ file
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

# Đọc ảnh từ file để hiển thị
image = cv2.imread(image_B_path)

# Tìm các khu vực chứa mặt người trong ảnh B
face_locations = face_recognition.face_locations(image)

# Chuyển đổi ảnh sang định dạng BGR để sử dụng với OpenCV
image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

# Vẽ hình chữ nhật xung quanh các khu vực chứa mặt người
for (top, right, bottom, left) in face_locations:
    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

# Hiển thị ảnh trong cửa sổ mới
cv2.imshow('Displayed Image', image)

# Chờ người dùng nhấn phím bất kỳ để đóng cửa sổ
cv2.waitKey(0)

# Đóng cửa sổ hiển thị
cv2.destroyAllWindows()
