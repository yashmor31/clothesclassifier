# -*- coding: utf-8 -*-
"""testing code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kTgsqcXNJadv7Xy5oZuLXNbJZw9_tce2
"""

import cv2
import os
import sys
import glob
import argparse
import numpy as np
from keras import backend as K
from keras.models import load_model
from keras.applications.resnet50 import preprocess_input
from keras.preprocessing import image

from google.colab import drive

drive.mount('/content/drive')

def get_files(path):
    path = 'drive/My Drive/dataset_path'
    if os.path.isdir(path):
        files = glob.glob(os.path.join(path, '*'))
    elif path.find('*') > 0:
        files = glob.glob(path)
    else:
        files = [path]

    files = [f for f in files if f.endswith('JPG') or f.endswith('jpg') or f.endswith('PNG') or f.endswith('png') or f.endswith('JPEG') or f.endswith('jpeg') or f.endswith('TIFF')]

    if not len(files):
        sys.exit('No images found by the given path!')

    return files

if __name__ == '__main__':
    args = parse_args()
    files = get_files(args.path)
    cls_list = ['34_sleeve', 'angel_sleeve', 'bell_sleeve', 'bishop_sleeve', 'butterfly_sleeve', 'cap_sleeve', 'cape_sleeve', 'cold-shoulder', 'kimono_sleeve', 'long_sleeve', 'puff_sleeve', 'short_sleeve', 'sleeveless']


    classify = load_model('modelresnet50.h5')



    for f in files:
        #img = image.load_img(f, target_size=(150,150))
        image1 = cv2.imread(f)
        image1 = cv2.resize(image1,(150,150))
        cv2.imwrite('test.jpg', image1)
        img = image.load_img('test.jpg')
        if img is None:
            continue
        x = image.img_to_array(img)
        x = preprocess_input(x)
        x = np.expand_dims(x, axis=0)
        pred = classify.predict(x)[0]
        top_inds = pred.argsort()[::-1][:5]
        print(f)
        for i in top_inds:
            print('    {:.2f}  {}'.format(pred[i], cls_list[i]))

!pip install argparse

import cv2
import os
import sys
import glob
import argparse
import numpy as np
from keras import backend as K
from keras.models import load_model
from keras.applications.resnet50 import preprocess_input
from keras.preprocessing import image

from google.colab import drive

drive.mount('/content/drive')

def get_files(path):
    path = 'drive/My Drive/dataset_path'
    if os.path.isdir(path):
        files = glob.glob(os.path.join(path, '*'))
    elif path.find('*') > 0:
        files = glob.glob(path)
    else:
        files = [path]

    files = [f for f in files if f.endswith('JPG') or f.endswith('jpg') or f.endswith('PNG') or f.endswith('png') or f.endswith('JPEG') or f.endswith('jpeg') or f.endswith('TIFF')]

    if not len(files):
        sys.exit('No images found by the given path!')

    return files

if __name__ == '__main__':
    args = parse_args()
    files = get_files(args.path)
    cls_list = ['34_sleeve', 'angel_sleeve', 'bell_sleeve', 'bishop_sleeve', 'butterfly_sleeve', 'cap_sleeve', 'cape_sleeve', 'cold-shoulder', 'kimono_sleeve', 'long_sleeve', 'puff_sleeve', 'short_sleeve', 'sleeveless']


    classify = load_model('modelresnet50.h5')

for f in files:
        #img = image.load_img(f, target_size=(150,150))
        image1 = cv2.imread(f)
        image1 = cv2.resize(image1,(150,150))
        cv2.imwrite('test.jpg', image1)
        img = image.load_img('test.jpg')
        if img is None:
            continue
        x = image.img_to_array(img)
        x = preprocess_input(x)
        x = np.expand_dims(x, axis=0)
        pred = classify.predict(x)[0]
        top_inds = pred.argsort()[::-1][:5]
        print(f)
        for i in top_inds:
            print('    {:.2f}  {}'.format(pred[i], cls_list[i]))

