import face_recognition
import cv2

# Mở luồng video từ webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Lấy khung hình từ video
    ret, frame = video_capture.read()

    # Chuyển đổi khung hình từ BGR (OpenCV sử dụng) sang RGB
    rgb_frame = frame[:, :, ::-1]

    # Phát hiện và mã hóa khuôn mặt trong khung hình
    face_locations = face_recognition.face_locations(rgb_frame)
    # face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Vẽ hình chữ nhật quanh các khuôn mặt phát hiện được
    for (top, right, bottom, left) in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    # Hiển thị video với khuôn mặt được phát hiện
    cv2.imshow('Video', frame)

    # Nhấn phím 'q' để thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên
video_capture.release()
cv2.destroyAllWindows()