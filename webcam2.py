import face_recognition
import cv2

# Import photo files and names of people in the known list
known_images = {
    'emma_watson1.png': "Emma Watson",
    'birain1.png': "Bi Rain",
    'timothee1.png': "Timotheé Chalamet",
    'Asha.jpg': "Asha",
    'Anna.jpg': "Anna"
}

# Load known faces and their encodings
known_face_encodings = []
known_face_names = []

for image_path, name in known_images.items():
    image = face_recognition.load_image_file(image_path)
    face_encoding = face_recognition.face_encodings(image)[0]
    known_face_encodings.append(face_encoding)
    known_face_names.append(name)

#Face recognition function
def recognize_faces_in_image(image_path):
    # Load the image to be recognized
    image_to_recognize = face_recognition.load_image_file(image_path)
    
    # Find all face locations and face encodings in the image
    face_locations = face_recognition.face_locations(image_to_recognize)
    face_encodings = face_recognition.face_encodings(image_to_recognize, face_locations)
    
    # Convert the image to BGR color (which OpenCV uses)
    image_to_recognize = cv2.cvtColor(image_to_recognize, cv2.COLOR_RGB2BGR)
    
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"
        
        if True in matches:
            matched_indexes = [i for i, match in enumerate(matches) if match]
            names = [known_face_names[i] for i in matched_indexes]
            name = ", ".join(names)
        
        # Draw a rectangle around the face
        cv2.rectangle(image_to_recognize, (left, top), (right, bottom), (0, 255, 0), 3)
        # Draw the name below the face
        cv2.putText(image_to_recognize, name, (left, bottom + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    # Display the image
    cv2.imshow('Recognized Faces', image_to_recognize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def recognize_faces_in_video():
    video_capture = cv2.VideoCapture(0)
    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    while True:
        result, video_frame = video_capture.read()
        if not result:
            break
        
        gray_image = cv2.cvtColor(video_frame, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
        
        for (x, y, w, h) in faces:
            face_image = video_frame[y:y+h, x:x+w]
            face_encodings = face_recognition.face_encodings(face_image)
            
            if face_encodings:
                face_encoding = face_encodings[0]
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"
                
                if True in matches:
                    matched_indexes = [i for i, match in enumerate(matches) if match]
                    names = [known_face_names[i] for i in matched_indexes]
                    name = ", ".join(names)
                
                # Draw a rectangle around the face
                cv2.rectangle(video_frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
                # Draw the name below the face
                cv2.putText(video_frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        cv2.imshow("Real-Time Face Recognition", video_frame)
        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    
    video_capture.release()
    cv2.destroyAllWindows()

# Main program
choice = input("Enter '1' to recognize faces from an image or '2' to use the webcam: ")

if choice == '1':
    image_path = input("Enter the name of the image file to be identified: ")
    recognize_faces_in_image(image_path)
elif choice == '2':
    recognize_faces_in_video()
else:
    print("Invalid choice. Please enter '1' or '2'.")
