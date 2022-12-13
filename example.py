from deepface import DeepFace

import os
path='/media/rutu/hdd/Reserach_work/AI project/deepface-master/crawling/images/'
images=os.listdir(path)
img='/media/rutu/hdd/Reserach_work/AI project/deepface-master/crawling/Test_imges/image_9.jpg'
for i in range(len(images)):
    image=path+images[i]


    result = DeepFace.verify(img1_path = img,
                         img2_path =image)
    if result['verified']==True:
        print("match")