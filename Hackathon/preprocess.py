import cv2
import csv
import os
import pickle

with open("D:\\PESU\\Sem_V\\AI\\Hackathon\\train.pickle", 'rb') as f:
    train = pickle.load(f)

for i in range(len(train)):
    train[i] = train[i].encode('ascii')
    
csvfile = open("dataset3.csv", 'w')

img_dir = "D:\\PESU\\Sem_V\\AI\\Hackathon\\data\\VOCdevkit\\VOC2010\\JPEGImages"
annotation_dir = "D:\\PESU\\Sem_V\\AI\\Hackathon\\data\\VOCdevkit\\VOC2010\\Annotations"

all_img = os.listdir(img_dir)

pixels = list(range(30000))
csvfile.write("Image," + (",".join(list(map(str, pixels)))) + '\n')

#count = 0
for i in all_img:
    if(i[:-4] in train):
        #count += 1
        
        image = os.path.join(img_dir, i)
        img = cv2.imread(image)
        small = cv2.resize(img, (100, 100)) 

        l = small.ravel()
        csvfile.write(str(i)[:-4] + "," + (",".join(list(map(str, l)))) + '\n')
        
csvfile.close()

#print(count)
#print(train[0:10], len(train))
