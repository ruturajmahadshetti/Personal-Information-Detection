import csv
import os
import glob
import pandas as pd
import os
from retinaface import RetinaFace

from deepface import DeepFace
path='/study/Ruturaj/Research work/AI_face_recognition/crawling/'
img='/study/Ruturaj/Research work/AI_face_recognition/images/img_24.jpg'
import cv2
pf=pd.read_csv(path+'Crawling_data.csv')
resize='/study/Ruturaj/Research work/AI_face_recognition/crawling/detection_result/'
img_list=pf['image_path']
web_page=pf['web_page']
urls=pf['url']
# import matplotlib.pyplot as plt
# from retinaface import RetinaFace
# resp = RetinaFace.detect_faces(img)
# print(resp)
# faces = RetinaFace.extract_faces(img_path = img, align = True)
# for face in faces:
#   plt.imshow(face)
#   plt.title('Face_output')
#   plt.show()
with open('/study/Ruturaj/Research work/AI_face_recognition/crawling/detection/filtered_data3.csv', 'w',
          newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["image_path", 'web_page', 'url'])
    for i in range(len(img_list)):


        images=path+img_list[i][2:]
        resize_name=resize+images[65:]
        print(resize_name)

        #
        output = RetinaFace.detect_faces(images)
        # # print(images)
        # # print(type(output))
        if type(output)==dict:
            im=cv2.imread(images)
            cv2.imwrite(resize_name,im)
            # print(type(im))
            writer.writerow([images,web_page[i], urls[i]])
    #
    # print(type(output))
    # if output[]:
    # #     print(images)
    # df = DeepFace.find(img_path=img, db_path="C:/workspace/my_db")

    # obj = DeepFace.verify(img, images
    #                       , model_name='SFace', detector_backend='retinaface')
    # if obj["verified"] == True :
    #     print(images,'Link:',web_page[i],urls[i])
