from tensorflow.keras.models import load_model
from face_main import Face_utils
import cv2
import numpy as np
import pickle

model = load_model('facenet_keras.h5')

path= "D:\\Facenet-Face_recognition\\nab1.jpg"

f = Face_utils()

image = cv2.imread(path)
boxes = f.detect_face(path)

box = boxes[0]

roi = f.return_face(image,box)
embedding = f.face_embedding(model,roi)
#print(face_pix.shape)
#print("sample ", sample.shape)
print(embedding))

