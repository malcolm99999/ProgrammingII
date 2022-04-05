import cv2
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

# https://stackoverflow.com/questions/34588464/python-how-to-capture-image-from-webcam-on-click-using-opencv

cam = cv2.VideoCapture(0)
cv2.namedWindow("Camera Window")

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")

    cv2.imshow("Camera Window", frame)
    k = cv2.waitKey(1)

    if k%256 == 32:
        # SPACE pressed
        cv2.imwrite("opencv_photo.png", frame)

        cam.release()
        cv2.destroyAllWindows()
        model = load_model('keras_model.h5')
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        image = Image.open('opencv_photo.png')
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        data[0] = normalized_image_array
        prediction = model.predict(data)
        print(prediction)
        exit()

