#FOLLIWING THE 	"Classifying ImageNet: the instant Caffe way" TUTORIAL
#AT http://nbviewer.ipython.org/github/BVLC/caffe/blob/master/examples/classification.ipynb

import cPickle
import gzip
import os
import sys
import time

import scipy
import scipy.ndimage

import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

# Make sure that caffe is on the python path:
caffe_root = '../../caffe-master/'
# this file is expected to be in {caffe_root}/examples

import sys
sys.path.insert(0, caffe_root + 'python')

import caffe

# Make sure that this first links to the 'caffe-master' directory 
# Set the right path to your model definition file, pretrained model weights,
# and the image you would like to classify.
MODEL_FILE = '../../caffe-master/models/bvlc_reference_caffenet/deploy.prototxt'
PRETRAINED = '../../caffe-master/models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel'
IMAGE_FILE = 'images/cat.jpg'

import os
#os.system("echo 'hello world'")
if not os.path.isfile(PRETRAINED):
    print("Downloading pre-trained CaffeNet model...")
    os.system("../../caffe-master/scripts/download_model_binary.py ../../caffe-master/models/bvlc_reference_caffenet")

caffe.set_mode_cpu()
net = caffe.Classifier(MODEL_FILE, PRETRAINED,
	                       mean=np.load(caffe_root + 'python/caffe/imagenet/ilsvrc_2012_mean.npy').mean(1).mean(1),
	                       channel_swap=(2,1,0),
	                       raw_scale=255,
	                       image_dims=(256, 256))

input_image = caffe.io.load_image(IMAGE_FILE)
plt.imshow(input_image)

prediction = net.predict([input_image])  # predict takes any number of images, and formats them for the Caffe net automatically
print 'prediction shape:', prediction[0].shape
plt.plot(prediction[0])
print 'predicted class:', prediction[0].argmax()
print(prediction[0])

#test commit

print '... hello world'


