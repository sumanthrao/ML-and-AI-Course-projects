import os
import xml.etree.ElementTree as ET
import csv
import pickle
from PIL import Image
import cv2

padded_images_dir = "D:\\PESU\\Sem_V\\AI\\Hackathon\\PaddedImages"

all_img = os.listdir(padded_images_dir)

csvfile = open("localization_dataset4.csv", 'w')

pixels = list(range(49152))
csvfile.write("Image," + (",".join(list(map(str, pixels)))) + '\n')

all_img = all_img[:1000]

#all_img = ['2008_000008.jpg']
for i in all_img:
    image = os.path.join(padded_images_dir, i)
    img = cv2.imread(image)

    l = img.ravel()
    csvfile.write(str(i)[:-4] + "," + (",".join(list(map(str, l)))) + '\n')

csvfile.close()
