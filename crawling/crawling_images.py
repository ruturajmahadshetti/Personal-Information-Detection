# First, you should install flickrapi
# pip install flickrapi
from retinaface import RetinaFace
import flickrapi
import urllib
import requests
from PIL import Image
import csv
import os
# Flickr api access key
flickr = flickrapi.FlickrAPI('c6a2c45591d4973ff525042472446ca2', '202ffe6f387ce29b', cache=True)

keyword = 'portrait'

photos = flickr.walk(text=keyword,
                     tag_mode='all',
                     tags=keyword,
                     extras='url_c',
                     per_page=200,  # may be you can try different numbers..
                     sort='relevance')

urls = []
for i, photo in enumerate(photos):

    # print(photos)
    url = photo.get('url_c')
    urls.append(url)

    # get 200 urls
    if i >= 4000:
        break
# print(urls)
# for i in range (len(urls)):
#     if not urls[i]==None:
#         print(urls[i])
counnt=0
media = 'https://www.flickr.com/'
with open('/study/Ruturaj/Research work/AI_face_recognition/crawling/Crawling_data.csv', 'w',
          newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["image_path", 'web_page', 'url'])
    source='/study/Ruturaj/Research work/AI_face_recognition/crawling'
    for i in range(len(urls)):
        if not urls[i]==None:
            path='./download/'
            img='img_'+str(i)+'.jpg'
            down_path=path+img

          # print(img)
            urllib.request.urlretrieve(urls[i], down_path)
            resize_path = './images/' + img
           # # Resize the image and overwrite it
            image = Image.open(down_path)
            i
            # resp = RetinaFace.detect_faces(image)
            image.save(resize_path)
            # print(down_path,media,urls[i])

            writer.writerow([resize_path,media, urls[i]])
#
