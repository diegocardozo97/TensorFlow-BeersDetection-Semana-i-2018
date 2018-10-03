import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import numpy as np

import glob, os, sys

import xml.etree.ElementTree as ET
import math


STEP = 8

# The path in the console arguments.
path = sys.argv[1]

imgs= sorted(glob.glob(os.path.join(path, '*.jpg')) + glob.glob(os.path.join(path, '*.JPG')))
xmls = sorted(glob.glob(os.path.join(path, '*.xml')) + glob.glob(os.path.join(path, '*.XML')))


for i in range(len(imgs)):
    print(imgs[i])
    
    img = mpimg.imread(imgs[i])
    size_orignal = img.shape[0] if img.shape[0] > img.shape[1] else img.shape[1]
    img = img[list(range(0, img.shape[0], STEP)),:,:]
    img = img[:,list(range(0, img.shape[1], STEP)),:]

    mpimg.imsave(imgs[i], img)


    tree = ET.parse(xmls[i])
    root = tree.getroot()

    ratio = math.ceil(size_orignal / img.shape[0]) 

    for size in root.iter('size'):
        size.find('width').text = str(img.shape[1])

        size.find('height').text = str(img.shape[0])

    for box in root.iter('bndbox'):
        x = str(int(box.find('xmin').text) // ratio)
        box.find('xmin').text = x

        y = str(int(box.find('ymin').text) // ratio)
        box.find('ymin').text = y

        x = str(int(box.find('xmax').text) // ratio)
        box.find('xmax').text = x

        y = str(int(box.find('ymax').text) // ratio)
        box.find('ymax').text = y


    tree.write(xmls[i])
