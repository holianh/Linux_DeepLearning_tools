# Flask server: predict an image

```python
# USAGE
# Start the server:
#     python server3.py
# Submit a request via cURL:
#     curl -X POST -F image=@image.jpg "http://localhost:5000/predict"
# Submita a request via Python:
#    python client3.py


import os
os.environ["CUDA_VISIBLE_DEVICES"]="0"
import cv2
import numpy as np
from os.path import join, exists
import numpy as np
import flask
import socket
import io
from keras.models import load_model
def TaResize(img):
    img = cv2.resize(img, (224,224), interpolation = cv2.INTER_AREA)
    return img
import cv2,os
from PIL import Image
app = flask.Flask(__name__)
print("load model:---------------------------------")

import os, io, json
from keras.models import model_from_json
import numpy as np

def myGet_weight(fnName_model,fmName_weight):
    # Ref:https://machinelearningmastery.com/save-load-keras-deep-learning-models/
    # load json and create model
    json_file = open(fnName_model, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights(fmName_weight)
    return loaded_model
    # WW = loaded_model.get_weights()
    # print("Loaded model from disk:",fmName_weight)
    # return np.asarray(WW)
#use: 
 
#loaddedmodel=load_model('./Model/ResNet50.h5')
fnName_model ='Model/ResNet50.h5.json'
fmName_weight='Model/ResNet50.h5.weight'
loaddedmodel=myGet_weight(fnName_model,fmName_weight)
loaddedmodel._make_predict_function()
print("Model loadded ------------------------------")


print('This server IP:',[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])



@app.route("/predict", methods=["POST"])
def predict():
    # initialize the data dictionary that will be returned from the view
    data = {"success": False}
    # ensure an image was properly uploaded to our endpoint
    if flask.request.method == "POST":
        if flask.request.files.get("image"):
            # read the image in PIL format
            image = flask.request.files["image"].read()
            img = Image.open(io.BytesIO(image))              
            img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            
            #img=cv2.imread(fn,cv2.IMREAD_COLOR)
            img=TaResize(img) #/255.0
            ff= np.expand_dims(img, axis=0); # print(ff.shape)
            pred=loaddedmodel.predict(ff) ; #print(pred[0])
            predMax=np.argmax(pred, axis=1)
            Name="Hand" if predMax[0]==1 else "No Hand"
            print("----------------------")
            print("Results:",Name)
            print("----------------------")
            
            data = {"success": Name,"probNo_Y":"{} {}".format( round(pred[0][0],3), round(pred[0][1],3) )}

    # return the data dictionary as a JSON response
    return flask.jsonify(data)

# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
    print(" Loading Keras model and Flask starting server...\nplease wait until server has fully started")
    # load_model()
    app.run()
ight("(ta1072.npy_1080ti-3).model.json","(ta1072.npy_1080ti-3).w.json")

```

# Flask Client 

```python
# USAGE
# python client3.py

# import the necessary packages
import requests

# initialize the Keras REST API endpoint URL along with the input
# image path
KERAS_REST_API_URL = "http://localhost:5000/predict"
IMAGE_PATH = "image.jpg"

# load the input image and construct the payload for the request
image = open(IMAGE_PATH, "rb").read()
payload = {"image": image}

# submit the request
r = requests.post(KERAS_REST_API_URL, files=payload).json()
print(r) #: result json:   {'probNo_Y': '0.0 1.0', 'success': 'Hand'}

```
