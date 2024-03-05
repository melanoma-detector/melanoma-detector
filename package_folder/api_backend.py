from fastapi import FastAPI
from package_folder.utils import from_number_to_string
#import tensorflow as tf
api = FastAPI()

# define a root `/` endpoint
@api.get("/")
def index():
    return {"greeting": "well done"}


@api.get("/predict")
def predict(feature1, feature2):

    #model = tf.keras.saving.load_model("the path to the model folder")
    #prediction = model.predict(inputs needed)
    #pretty_prediction = from_number_to_string(float(prediction[0]))

    # Here, I'm only returning the features, since I don't actually have a model.
    # In a real life setting, you would return the predictions.
    #return {'prediction': pretty_prediction}
    return {'prediction': int(feature1)*int(feature2)}
