from keras.models import load_model
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense

from keras.preprocessing.image import img_to_array, load_img
import numpy as np
import tensorflow as tf

# dimensions of our images.
img_width, img_height = 150, 150

input_shape = (img_width, img_height, 3)
test_model = Sequential()

test_model.add(Conv2D(32, (3, 3), input_shape=input_shape))
test_model.add(Activation('relu'))
test_model.add(MaxPooling2D(pool_size=(2, 2)))

test_model.add(Conv2D(32, (3, 3)))
test_model.add(Activation('relu'))
test_model.add(MaxPooling2D(pool_size=(2, 2)))

test_model.add(Conv2D(64, (3, 3)))
test_model.add(Activation('relu'))
test_model.add(MaxPooling2D(pool_size=(2, 2)))

test_model.add(Flatten())
test_model.add(Dense(64))
test_model.add(Activation('relu'))
test_model.add(Dropout(0.5))
test_model.add(Dense(1))
test_model.add(Activation('sigmoid'))

test_model = load_model('first_model.h5')
def predict(basedir, model):
    for i in range(4001,4040):
        path = basedir + str(i) + '.jpg'

        img = load_img(path,False,target_size=(img_width,img_height))
        x = img_to_array(img)
        x = x/255
        x = np.expand_dims(x, axis=0)
        preds = model.predict_classes(x)
        probs = model.predict_proba(x)
        if preds == 1:
            out = "dog"
        else:
            out = "cat"
        print(str(probs) + " " + str(preds) + " " + out)

print ("predict cats")
basedir = "data/test/cat."
predict(basedir, test_model)

print ("predict dogs")

basedir = "data/test/dog."
predict(basedir, test_model)

print('done')
