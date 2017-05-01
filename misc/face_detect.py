import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(
        frame, scaleFactor=1.2, minSize=(20, 20))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255))

    kernel = np.ones((21, 21), 'uint8')
    for (x, y, w, h) in faces:
        frame[y:y + h, x:x + w,
           :] = cv2.dilate(frame[y:y + h, x:x + w, :], kernel)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255))

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
