# Khai báo thư viện
import face_recognition
import cv2

# Nhập tên file ảnh
image_path = 'people.png'

# Đọc ảnh từ file
image = face_recognition.load_image_file(image_path)

# Tìm các khu vực chứa mặt người
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
