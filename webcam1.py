import face_recognition
import cv2

# Import photo files and names of people in the known list
known_images = {
    'emma_watson1.png': "Emma Watson",
    'timothee1.png': "Timothee Chalamet",
    'Asha.jpg': "Asha",
    'Anna.jpg': "Anna",
    'My2.JPG' : "Diem My"
}

# Load known faces and their encodings
known_face_encodings = []
known_face_names = []

for image_path, name in known_images.items():
    image = face_recognition.load_image_file(image_path)
    face_encodings = face_recognition.face_encodings(image)
    if face_encodings:
        known_face_encodings.append(face_encodings[0])
        known_face_names.append(name)

# Mở luồng video từ webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Lấy khung hình từ video
    ret, frame = video_capture.read()

    # Chuyển đổi khung hình từ BGR (OpenCV sử dụng) sang RGB
    rgb_frame = frame[:, :, ::-1]

    # Phát hiện và mã hóa khuôn mặt trong khung hình
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Vẽ hình chữ nhật quanh các khuôn mặt phát hiện được và hiển thị tên
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Vẽ hình chữ nhật quanh khuôn mặt
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        # Hiển thị tên bên dưới khuôn mặt
        cv2.putText(frame, name, (left, bottom + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Hiển thị video với khuôn mặt được phát hiện
    cv2.imshow('Video', frame)

    # Nhấn phím 'q' để thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên
video_capture.release()
cv2.destroyAllWindows()
