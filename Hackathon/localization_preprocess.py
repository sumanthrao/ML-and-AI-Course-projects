import os
import xml.etree.ElementTree as ET
import csv
import pickle
from PIL import Image

img_dir = "D:\\PESU\\Sem_V\\AI\\Hackathon\\data\\VOCdevkit\\VOC2010\\JPEGImages"
annotation_dir = "D:\\PESU\\Sem_V\\AI\\Hackathon\\data\\VOCdevkit\\VOC2010\\Annotations"
padded_images_dir = "D:\\PESU\\Sem_V\\AI\\Hackathon\\PaddedImages"

with open("D:\\PESU\\Sem_V\\AI\\Hackathon\\image_names.pickle", 'rb') as f:
    train = pickle.load(f)

for i in range(len(train)):
    train[i] = train[i].encode('ascii')

all_img = os.listdir(img_dir)

for i in all_img:
    if(i[:-4] in train):
        #count += 1
        image = os.path.join(img_dir, i)
        img = Image.open(image)
        small = img.resize((int(img.size[0]*0.25) ,int(img.size[1]*0.25))) 
        
        new_img = Image.new(mode = "RGB", size=(128,128))
        new_img.paste(small, (0, 0))
        new_img.save(os.path.join(padded_images_dir, i))
