import csv
import os
import glob
import pandas as pd
import os
from tqdm import tqdm
from retinaface import RetinaFace

from deepface import DeepFace
path='/study/Ruturaj/Research work/AI_face_recognition/crawling/'
img='/home/hoangthu/Desktop/img_9.jpg'
img1='/study/Ruturaj/Research work/AI_face_recognition/crawling/images/img_98.jpg'
# img='/study/Ruturaj/Research work/AI_face_recognition/crawling/images/img_13.jpg'
import cv2
pf=pd.read_csv(path+'filtered_data.csv')

img_list=pf['image_path']
web_page=pf['web_page']
urls=pf['url']
w=[]
l=[]
imgs='/study/Ruturaj/Research work/AI_face_recognition/crawling/detection_result'
for i in tqdm(range(len(img_list))):

    images=img_list[i]
    # print(images)

    obj = DeepFace.verify(img1, images
                          , model_name='SFace', detector_backend='retinaface',distance_metric ='euclidean_l2')
    # print(obj)
    if obj["verified"] == True :
        print(images,'Link:',web_page[i],urls[i])
        w.append(web_page[i])
        l.append(urls[i])
print("w :",w)
print('l',l)
