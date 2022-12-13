from deepface.basemodels import SFace,VGGFace
import pandas as pd
import numpy as np
from retinaface import RetinaFace
import cv2

path = '/study/Ruturaj/Research work/AI_face_recognition/crawling/detection/'
pf = pd.read_csv(path + 'filtered_data.csv')

img_list = pf['image_path']
from retinaface import RetinaFace
model = VGGFace.loadModel()
input_shape = model.layers[0].input_shape[1:3]
# print(input_shape)
representations = []
img=img_list[1]
print(img)
faces= RetinaFace.extract_faces(img)
for face in faces:
    im = cv2.resize(face, (224, 224))

