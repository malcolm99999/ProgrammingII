import cv2

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('RDJ.png')
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_coordinates = trained_face_data.detectMultiScale(greyscaled_img)

(x, y, w, h) = face_coordinates
cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow('Astute Programmer Face Detector ', img)
cv2.waitKey()

print("Code Complete")