"""Script para detecção de gatos com alarme."""

import cv2
import os

# import winsound


def alarme():
    """Alarme em caso de detecção."""
    # winsound.Beep(2000, 100)  # Para Windows
    duration = 0.2  # seconds
    freq = 440  # Hz
    os.system(f'play -nq -t alsa synth {duration} sine {freq}')
    # os.system('spd-say "cat"')


face_cascade = cv2.CascadeClassifier(
    'haarcascade/haarcascade_frontalcatface.xml'
)

url = 0
# url = 'http://192.168.1.75:8080/video'
cap = cv2.VideoCapture(url)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for x, y, w, h in faces:
        alarme()
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(
            img,
            'Gato',
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
        )
        roi_gray = gray[y:y+h, x:x+w]

        roi_face = img[y:y+h, x:x+w]

    # img = cv2.resize(img, (800, 450))
    cv2.imshow('Captura', img)
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
