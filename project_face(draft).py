import face_recognition
import cv2

"""
Nhận diện và so sánh khuôn mặt:
Phân tích và so sánh khuôn mặt được phát hiện với các khuôn mặt đã biết (từ ảnh mẫu) 
để xác định liệu khuôn mặt đó có khớp với bất kỳ ai trong danh sách đã biết hay không.
"""
#Nhập file ảnh và tên của những người trong danh sách đã biết
image_Emma_path = 'emma_watson1.png'
name_Emma = "Emma Watson"

image_Rain_path = 'birain1.png'
name_Rain = "Bi Rain"

image_Timothee_path = 'timothee1.png'
name_Timothee = "Timotheé Chalamet"

#Nhập tên file ảnh cần xác định
image_define_path = input("Nhập tên file ảnh cần xác định: ")
#image_define_path = 'blackpink.png'

#Đọc ảnh từ file
image_Emma = face_recognition.load_image_file(image_Emma_path)
image_Rain = face_recognition.load_image_file(image_Rain_path)
image_Timothee = face_recognition.load_image_file(image_Timothee_path)
image_define = face_recognition.load_image_file(image_define_path)

#Mã hoá khuôn mặt trong các ảnh thuộc danh sách đã biết
#face_encoding_A = face_recognition.face_encodings(image_A)[0]
face_encoding_Emma = face_recognition.face_encodings(image_Emma)[0]
face_encoding_Rain = face_recognition.face_encodings(image_Rain)[0]
face_encoding_Timothee = face_recognition.face_encodings(image_Timothee)[0]

#Mã hoá khuôn mặt trong ảnh cần xác định
face_encoding_define = face_recognition.face_encodings(image_define)[0]

#So sánh khuôn mặt cần xác định với các khuôn mặt trong danh sách đã biết
#Tạo một danh sách các khuôn mặt đã biết và tên tương ứng
known_face_encodings = [face_encoding_Emma, face_encoding_Rain, face_encoding_Timothee]
known_face_names = [name_Emma, name_Rain, name_Timothee]

# So sánh khuôn mặt cần xác định với các khuôn mặt trong danh sách đã biết
results = face_recognition.compare_faces(known_face_encodings, face_encoding_define)

# Kiểm tra kết quả và in ra thông báo
if True in results:
    matched_index = results.index(True)
    name = known_face_names[matched_index]
    print(f"Người trong ảnh là {name}.")
else:
    print("Người trong ảnh không có tên trong danh sách đã biết.")

#Đọc ảnh từ file để hiển thị
image = cv2.imread(image_define_path)

#Tìm các khu vực chứa mặt người trong ảnh cần xác định
face_locations = face_recognition.face_locations(image)

#Chuyển đổi ảnh sang định dạng BGR để sử dụng với OpenCV
image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

#Vẽ hình chữ nhật xung quanh các khu vực chứa mặt người
for (top, right, bottom, left) in face_locations:
    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

#Hiển thị ảnh trong cửa sổ mới
cv2.imshow('Displayed Image', image)

#Chờ người dùng nhấn phím bất kỳ để đóng cửa sổ
cv2.waitKey(0)

#Đóng cửa sổ hiển thị
cv2.destroyAllWindows()

