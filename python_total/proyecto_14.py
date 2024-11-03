# Reconocimiento de rostros

import os
import datetime
import cv2
import face_recognition as fr


def load_and_process_picture(_path):

    picture = fr.load_image_file(_path)
    picture = cv2.cvtColor(picture, cv2.COLOR_BGR2RGB)  # From BGR to RGB format
    face = fr.face_locations(picture)[0]  # Locate face in picture (top right bottom left)
    face_code = fr.face_encodings(picture)[0]
    cv2.rectangle(picture,
                  (face[3], face[0]),  # left top
                  (face[1], face[2]),  # right bottom
                  (0, 255, 0),
                  1)
    return [picture, face_code]


employees = {}
for i in os.walk('data\\proyecto_14\\Empleados'):
    for j in i[2]:
        employees[j[:-4]] = load_and_process_picture(str(i[0] + '\\' + j))

success = False
while not success:
    image_captured = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    success, picture_captured = image_captured.read()
    if success:
        face_captured = fr.face_locations(picture_captured)
        if len(face_captured) == 0:
            success = False

face_captured = face_captured[0]
face_captured_code = fr.face_encodings(picture_captured)[0]
cv2.rectangle(picture_captured,
              (face_captured[3], face_captured[0]),  # left top
              (face_captured[1], face_captured[2]),  # right bottom
              (0, 255, 0),
              1)
match = False
for key in employees:

    face_distance = fr.face_distance([employees[key][1]], face_captured_code)
    print(key, face_distance)

    if face_distance < 0.68:

        registry_file = open('data\\proyecto_14\\registro.csv', 'w')
        registry_file.write(f"{datetime.datetime.now().strftime('%d/%m/%y %H:%M')};{key}")
        registry_file.close()

        match = True
        cv2.imshow(f'Bienvenido {key}', employees[key][0])
        cv2.waitKey()

        break

if not match:
    print('No hay ninguna coincidencia')


