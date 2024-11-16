"""
Program: project_face_recognition.py
Author: Mai Ngoc Diem My
Last date modified: 19/09/2024
The purpose of this program is takes as inputs a picture of people's face (or use webcam) and then analyze and compare the 
detected face with known faces (from sample images) to determine whether the face matches anyone on the known 
list to determine identity.
"""
import face_recognition
import cv2

# Import photo files and names of people in the known list
known_images = {
    'emma_watson1.png': "Emma Watson",
    'timothee1.png': "Timothee Chalamet",
    'Asha.jpg': "Asha",
    'Anna.jpg': "Anna",
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

# Face recognition function
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
            print(f"The person in the picture is {name}.")
        else:
            print("The person in the photo is not on the known list.")
        
        # Draw a rectangle around the face
        cv2.rectangle(image_to_recognize, (left, top), (right, bottom), (0, 255, 0), 3)
        # Draw the name below the face
        cv2.putText(image_to_recognize, name, (left, bottom + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    # Display the image
    cv2.imshow('Recognized Faces', image_to_recognize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Video function
def recognize_faces_in_video():
    # Open video stream from webcam
    video_capture = cv2.VideoCapture(0)

    while True:
        # Get frames from video
        ret, frame = video_capture.read()

        # Convert frame from BGR (OpenCV uses) to RGB
        rgb_frame = frame[:, :, ::-1]

        # Detect and encode faces in frames
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        # Match detected faces with known faces
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Draw a rectangle around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Show name below face
        cv2.putText(frame, name, (left, bottom + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Show video with detected face
        cv2.imshow('Video', frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Free up resources
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



