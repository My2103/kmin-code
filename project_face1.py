"""
Program: project_face_recognition.py
Author: Mai Ngoc Diem My
Last date modified:
The purpose of this program is takes as inputs a picture of people face and then analyze and compare the 
detected face with known faces (from sample images) to determine whether the face matches anyone on the known 
list to determine identity.
"""
import face_recognition
import cv2

"""
1. Nhận diện và so sánh khuôn mặt:
Phân tích và so sánh khuôn mặt được phát hiện với các khuôn mặt đã biết (từ ảnh mẫu) 
để xác định liệu khuôn mặt đó có khớp với bất kỳ ai trong danh sách đã biết hay không.

2. Nhận diện nhiều khuôn mặt trong một hình ảnh:
Phát hiện và nhận diện nhiều khuôn mặt trong cùng một bức ảnh. 
Mỗi khuôn mặt được nhận diện sẽ được so sánh với danh sách khuôn mặt đã biết để xác định danh tính.
"""
# Import photo files and names of people in the known list
image_Emma_path = 'emma_watson1.png'
name_Emma = "Emma Watson"

image_Rain_path = 'birain1.png'
name_Rain = "Bi Rain"

image_Timothee_path = 'timothee1.png'
name_Timothee = "Timotheé Chalamet"

image_Asha_path = 'Asha.jpg'
name_Asha = "Asha"

image_Anna_path = 'Anna.jpg'
name_Anna = "Anna"

# Enter the name of the image file to be identified
image_define_path = input("Enter the name of the image file to be identified: ")

# Read image from file
image_Emma = face_recognition.load_image_file(image_Emma_path)
image_Rain = face_recognition.load_image_file(image_Rain_path)
image_Timothee = face_recognition.load_image_file(image_Timothee_path)
image_Asha = face_recognition.load_image_file(image_Asha_path)
image_Anna = face_recognition.load_image_file(image_Anna_path)
image_define = face_recognition.load_image_file(image_define_path)

# Encoding faces in images from a known list
face_encoding_Emma = face_recognition.face_encodings(image_Emma)[0]
face_encoding_Rain = face_recognition.face_encodings(image_Rain)[0]
face_encoding_Timothee = face_recognition.face_encodings(image_Timothee)[0]
face_encoding_Asha = face_recognition.face_encodings(image_Asha)[0]
face_encoding_Anna = face_recognition.face_encodings(image_Anna)[0]

# Create a list of known faces and their corresponding names
known_face_encodings = [face_encoding_Emma, face_encoding_Rain, face_encoding_Timothee, face_encoding_Asha, face_encoding_Anna]
known_face_names = [name_Emma, name_Rain, name_Timothee, name_Asha, name_Anna]

# Find areas containing human faces in the image to be identified
face_locations = face_recognition.face_locations(image_define)
face_encodings_define = face_recognition.face_encodings(image_define, face_locations)

# Convert image to BGR format for use with OpenCV
image = cv2.cvtColor(image_define, cv2.COLOR_RGB2BGR)

# Vẽ hình chữ nhật xung quanh các khu vực chứa mặt người và xác định danh tính
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings_define):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    
    name = "Unknown" #Declare variable name

    # If a matching face is found, get the corresponding name.
    if True in matches:
        matched_indexes = [i for i, match in enumerate(matches) if match]
        names = [known_face_names[i] for i in matched_indexes]
        name = ", ".join(names)
        print(f"The person in the picture is {name}.")
    else:
        print("The person in the photo is not on the known list.")

    # Draw a rectangle around the face
    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 3)

    # Draw the person's name below the rectangle
    cv2.putText(image, name, (left, bottom + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Show image in new window
cv2.imshow('Displayed Image', image)

# Wait for the user to press any key to close the window
cv2.waitKey(0)

# Close display window
cv2.destroyAllWindows()

