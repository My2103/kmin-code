import face_recognition
import cv2

# Nhập file ảnh và tên của những người trong danh sách đã biết
image_Emma_path = 'emma_watson1.png'
name_Emma = "Emma Watson"

image_Rain_path = 'birain1.png'
name_Rain = "Bi Rain"

image_Timothee_path = 'timothee1.png'
name_Timothee = "Timotheé Chalamet"

# Đọc ảnh từ file
image_Emma = face_recognition.load_image_file(image_Emma_path)
image_Rain = face_recognition.load_image_file(image_Rain_path)
image_Timothee = face_recognition.load_image_file(image_Timothee_path)

# Mã hoá khuôn mặt trong các ảnh thuộc danh sách đã biết
face_encoding_Emma = face_recognition.face_encodings(image_Emma)[0]
face_encoding_Rain = face_recognition.face_encodings(image_Rain)[0]
face_encoding_Timothee = face_recognition.face_encodings(image_Timothee)[0]

# Tạo một danh sách các khuôn mặt đã biết và tên tương ứng
known_face_encodings = [face_encoding_Emma, face_encoding_Rain, face_encoding_Timothee]
known_face_names = [name_Emma, name_Rain, name_Timothee]

# Khởi tạo webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Lấy một khung hình từ webcam
    ret, frame = video_capture.read()

    # Chuyển đổi khung hình từ BGR (OpenCV) sang RGB (face_recognition)
    rgb_frame = frame[:, :, ::-1]

    # Tìm các khu vực chứa mặt người trong khung hình hiện tại
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Vẽ hình chữ nhật xung quanh các khu vực chứa mặt người và xác định danh tính
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # Nếu tìm thấy khuôn mặt khớp, lấy tên tương ứng
        if True in matches:
            matched_indexes = [i for i, match in enumerate(matches) if match]
            names = [known_face_names[i] for i in matched_indexes]
            name = ", ".join(names)
            print(f"Người trong ảnh là {name}.")
        else:
            print("Người trong ảnh không có tên trong danh sách đã biết.")

        # Vẽ hình chữ nhật xung quanh khuôn mặt
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 0), 2)

        # Vẽ tên của người dưới hình chữ nhật
        cv2.putText(frame, name, (left, bottom + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

    # Hiển thị khung hình với các khuôn mặt được nhận diện
    cv2.imshow('Video', frame)

    # Nhấn 'q' để thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng webcam và đóng cửa sổ hiển thị
video_capture.release()
cv2.destroyAllWindows()
