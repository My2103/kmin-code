#print_pic.py: Cho phep nhap vao file anh. Hien thi buc anh do ra man hinh

#import cv2 
#print(cv2.__version__)

# Khai báo thư viện
import cv2

# Đọc ảnh từ file
image = cv2.imread('IMG_5432.JPG')

# Start coordinate, here (5, 5)
# represents the top left corner of rectangle
start_point = (100, 100)

# Ending coordinate, here (220, 220)
# represents the bottom right corner of rectangle
end_point = (300, 360)

# Blue color in BGR
color = (255, 0, 0)

# Line thickness of 2 px
thickness = 2

# Using cv2.rectangle() method
# Draw a rectangle with blue line borders of thickness of 2 px
image = cv2.rectangle(image, start_point, end_point, color, thickness)

# Hiển thị ảnh trong cửa sổ mới
cv2.imshow('Displayed Image', image)

# Chờ người dùng nhấn phím bất kỳ để đóng cửa sổ
cv2.waitKey(0)

# Đóng cửa sổ hiển thị
cv2.destroyAllWindows()
