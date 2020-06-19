import cv2

# Create a CascadeClassifier Object
face_cascade = cv2.CascadeClassifier(
    "C:\\Users\\chris\\Documents\\github\\Edureka-OpenCV-Tutorial\\haarcascade_frontalface_default.xml")

# Reading the image as it is
img = cv2.imread("C:\\Users\\chris\\Pictures\\imageProcess\\nup.jpg", 1)

# Reading the image as a gray scale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Searching the co-ordinates of the image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

print(type(faces))
print(faces)

# Add rectangular face box around it
for x, y, w, h, in faces:
    img = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3)

resized = cv2.resize(img, (int(img.shape[1]), int(img.shape[0])))

cv2.imshow("Gray", resized)

cv2.waitKey(0)  # Wait until key is pressed
