import cv2
import face_recognition as fr


def load_picture(_path):

    picture = fr.load_image_file(_path)
    picture = cv2.cvtColor(picture, cv2.COLOR_BGR2RGB)  # From BGR to RGB format
    return picture


def locate_face(picture):

    face = fr.face_locations(picture)[0]  # Locate face in picture (top right bottom left)
    face_code = fr.face_encodings(picture)[0]
    cv2.rectangle(picture,
                  (face[3], face[0]),  # left top
                  (face[1], face[2]),  # right bottom
                  (0, 255, 0),
                  1)
    return picture, face_code


# Load control picture
picture_control = load_picture('data/proyecto_14/FotoA.jpg')
face_control, face_control_code = locate_face(picture_control)

# Load picture to compare vs control one
picture_test = load_picture('data/proyecto_14/FotoC.jpg')
face_test, face_test_code = locate_face(picture_test)

# Check if both pictures have the same face
distance_faces = fr.face_distance([face_control_code], face_test_code)
same_face = fr.compare_faces([face_control_code], face_test_code, 0.5)  # default 0.6

# Show picture and result of comparison
cv2.putText(face_test,
            f'{distance_faces.round(4)} : {same_face}',
            (20, 30),
            cv2.FONT_HERSHEY_PLAIN,
            1,
            (0, 255, 0),
            1)
cv2.imshow('Foto a Comparar', face_test)  # Show picture in screen

cv2.waitKey()
