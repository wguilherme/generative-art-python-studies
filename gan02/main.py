# import mtcnn
# fix import mtcnn
from mtcnn.mtcnn import MTCNN
import cv2
print(mtcnn.__version__)
# prepare model
model = MTCNN()
# detect face in the image
faces = model.detect_faces(pixels)
# extract details of the face
x1, y1, width, height = faces[0]['box']