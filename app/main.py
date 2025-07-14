
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = load_model("waste_classifier.keras")
class_names = ['Biodegradable', 'Non-Biodegradable']
recycling_tips = {
    'Biodegradable': "🌱 Compost kitchen/garden waste. Avoid plastic contamination.",
    'Non-Biodegradable': "♻️ Recycle plastics, metals, and e-waste through certified centers."
}

@app.post("/predict/")
async def predict_image(file: UploadFile = File(...)):
    image = Image.open(file.file).convert("RGB")
    image = image.resize((224, 224))
    image = img_to_array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    prediction = model.predict(image)[0]
    label = class_names[np.argmax(prediction)]
    confidence = float(np.max(prediction))

    return {
        "class": label,
        "confidence": confidence,
        "tip": recycling_tips[label]
    }
