import cv2

# coloured image
img = cv2.imread("C:\\Users\\chris\\Pictures\\imageProcess\\nup.jpg", 1)

# print image
print(img)

# type of image
print(type(img))

# size f image
print(img.shape)

# Resize the image by dividing original image by two
resized = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

# Displaying the image
cv2.imshow("Nup", resized)
cv2.waitKey(0)  # user has to press a key

cv2.destroyAllWindows()
