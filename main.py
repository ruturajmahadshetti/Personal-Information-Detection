from flask import Flask, render_template,request
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
import numpy as np
from wtforms.validators import InputRequired
from PIL import Image
import cv2
import pandas as pd
from deepface import DeepFace
import retinaface
from tqdm import tqdm
import deepface
path = '/study/Ruturaj/Research work/AI_face_recognition/crawling/detection/'
pf = pd.read_csv(path + 'filtered_data.csv')

img_list = pf['image_path']
web_page = pf['web_page']
urls = pf['url']



app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'upload'

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route('/', methods=['GET',"POST"])
@app.route('/home', methods=['GET',"POST"])
def home():

    form = UploadFileForm()
    if form.validate_on_submit():
        web = []
        link_images = []
        file = form.file.data # First grab the file
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # Then save the file
        uploaded_files = request.files.getlist("file")
        content = list()

        for uploaded_file in uploaded_files:
            image = Image.open(uploaded_file).convert('RGB')
            image = np.asarray(image)
            w = []
            l = []
            for i in range(len(img_list)):

                images = img_list[i]
                # print(images)

                obj = DeepFace.verify(image, images
                                      , model_name='SFace', detector_backend='retinaface')
                if obj["verified"] == True:
                    w.append(web_page[i])
                    link=urls[i]
                    l.append(link)

                    print(images, 'Link:', web_page[i], urls[i])

            length = len(l)
            return render_template('result.html',total_img=length,w=w,l=l)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)