'''
A special tool from quiver
Github repo: https://github.com/keplr-io/quiver
'''
from quiver_engine import server

from yolo3.model import yolo_eval, yolo_body, tiny_yolo_body
from keras.layers import Input
import os

num_anchors = 9
num_classes = 80
h5_path = './model/yolov3.h5'
input_shape = 416
model = yolo_body(Input(shape=(input_shape,input_shape,3)), num_anchors//3, num_classes)
model.load_weights(h5_path)

server.launch(
        model, # a Keras Model

        # classes, # list of output classes from the model to present (if not specified 1000 ImageNet classes will be used)

        # top, # number of top predictions to show in the gui (default 5)

        # where to store temporary files generatedby quiver (e.g. image files of layers)
        temp_folder='./tmp',

        # a folder where input images are stored
        input_folder='C:/Users/vcl/Desktop/PyTorch-YOLOv3/data/samples/',

        # the localhost port the dashboard is to be served on
        port=5000,
        # custom data mean
        mean=[123.568, 124.89, 111.56],
        # custom data standard deviation
        std=[52.85, 48.65, 51.56]
    )