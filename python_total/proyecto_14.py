import cv2
import face_recognition as fr


def load_picture(_path):
    picture = fr.load_image_file(_path)
    picture = cv2.cvtColor(picture, cv2.COLOR_BGR2RGB)  # From BGR to RGB format
    return picture


def locate_face(_name, picture):
    face = fr.face_locations(picture)[0]
    face_code = fr.face_encodings(picture)[0]
    cv2.rectangle(picture,
                  (face[3], face[0]),
                  (face[1], face[2]),
                  (0, 255, 0),
                  2)
    cv2.imshow(_name, picture)  # Show picture in screen


picture_control = load_picture('data/proyecto_14/FotoA.jpg')
locate_face('Foto de Control', picture_control)
# picture_test = load_picture('Foto de Prueba', 'data/proyecto_14/FotoB.jpg')


cv2.waitKey()
