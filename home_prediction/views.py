from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import numpy as np
import tensorflow as tf
from keras.preprocessing import image
import json


img_height, img_width = 256, 256

with open('./models/class_names.json', 'r') as f:
    labelInfo = f.read()

labelInfo = json.loads(labelInfo)

model = tf.keras.models.load_model('./models/plant_care_model.h5')


def index(request):
    return render(request, 'index.html')


def predictImage(request):
    if request.method == 'POST':

        fileObj = request.FILES['filePath']
        fs = FileSystemStorage()
        filePathNames = fs.save(fileObj.name, fileObj)
        filePathName = './media/' + filePathNames

        testimage = filePathName

        img = image.load_img(testimage, target_size=(img_height, img_width))
        x = image.img_to_array(img)

        x = x / 255
        x = x.reshape(1, img_height, img_width, 3)
        predictions = model.predict(x)

        predictedLabel = labelInfo[str(np.argmax(predictions[0]))]
        predictedLabel = results(predictedLabel)
        confidence = round(100 * (np.max(predictions[0])), 2)
  

        context = {'filePathName': filePathName, 'predictedLabel': predictedLabel, "predictions":predictions, 'confidence':confidence}
        return render(request, 'index.html', context)


def results(predictedLabel):
    if predictedLabel[0] == 'Corn_Blight':
        return 'This image shows, it is a corn leaf with blight disease.'
    elif predictedLabel[0] == 'Corn_Common_Rust':
        return 'This image shows, it is a corn leaf with common rust disease.'
    elif predictedLabel[0] == 'Corn_Healthy':
        return 'This image shows, it is a healthy corn leaf.'
    elif predictedLabel[0] == 'Mango_Anthracnose':
        return 'This image shows, it is a mango leaf with anthracnose disease.'
    elif predictedLabel[0] == 'Mango_Healthy':
        return 'This image shows, it is a healthy mango leaf.'
    elif predictedLabel[0] == 'Potato_Early_Blight':
        return 'This image shows, it is a potato leaf with early blight disease.'
    elif predictedLabel[0] == 'Potato_Healthy':
        return 'This image shows, it is a healthy potato leaf.'
    elif predictedLabel[0] == 'Potato_Late_Blight':
        return 'This image shows, it is a potato leaf with late blight disease.'
    elif predictedLabel[0] == 'Tomato_Early_blight':
        return 'This image shows, it is a tomato leaf with early blight disease.'
    elif predictedLabel[0] == 'Tomato_healthy':
        return 'This image shows, it is a healthy tomato leaf.'
    elif predictedLabel[0] == 'Tomato_Late_blight':
        return 'This image shows, it is a tomato leaf with late blight disease.'
    elif predictedLabel[0] == 'Tomato_Target_Spot':
        return 'This image shows, it is a tomato leaf with target spot disease.'
    elif predictedLabel[0] == 'Wheat_Brown_Rust':
        return 'This image shows, it is a wheat leaf with brown rust disease.'
    elif predictedLabel[0] == 'Wheat_Healthy':
        return 'This image shows, it is a healthy wheat leaf.'
    else: 
        return 'This image shows, it is a wheat leaf with yellow rust disease.'