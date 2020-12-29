'''
Need to install some package:

pip install pydot
pip install pydotplus
pip install graphviz

Download Binary graphviz follow: https://graphviz.org/download/
Link instruction: https://stackoverflow.com/questions/47605558/importerror-failed-to-import-pydot-you-must-install-pydot-and-graphviz-for-py
Then add bin of graphviz to PATH if on windows
Or add directly on code follow StackOverFlow question (https://stackoverflow.com/questions/60177398/keras-or-tensorflow-function-to-draw-a-3d-diagram-of-a-neural-network-structure)
'''

from tensorflow.keras.utils import plot_model as plt
# from yolo import *
from yolo3.model import yolo_eval, yolo_body, tiny_yolo_body
from keras.layers import Input
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'


num_anchors = 9
num_classes = 80
h5_path = r'E:\model\yolo\test.h5'
input_shape = 416
model = yolo_body(Input(shape=(input_shape,input_shape,3)), num_anchors//3, num_classes)
model.load_weights(h5_path)
# y = YOLO()
# model = y.yolo_model
# model.summary()
plt(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)