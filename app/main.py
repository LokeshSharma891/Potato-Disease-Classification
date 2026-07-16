from io import BytesIO
import numpy as np
import uvicorn
from PIL import Image
from fastapi import FastAPI, UploadFile, File
import tensorflow as tf
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from tensorflow import keras
MODEL = keras.models.load_model("../models/model_v2.keras")


CLASS_NAMES = ["Early Blight" , "Late Blight" , "Healthy" ]
@app.get("/ping")
async def ping():
    return {"ping": "pong"}

def readfileasimage(data) -> np.ndarray:
   image = np.array (Image.open(BytesIO(data)))
   return image
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = readfileasimage(await file.read())
    img_batch = np.expand_dims(image, axis=0)
    prediction = MODEL.predict(img_batch)
    predicted_class = CLASS_NAMES[np.argmax(prediction[0])]
    confidence = np.max(prediction[0])
    return{
        'class' : predicted_class,
        'confidence' : float(confidence)
    }

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)