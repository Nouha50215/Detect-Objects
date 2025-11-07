# FastAPI app entry (defines routes)

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from . import model
from . import utils

app = FastAPI(title="Object Detection API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/detect")
async def detect_object(file: UploadFile = File(...)):
    image_bytes = await file.read()
    result_json, annotated_image = model.predict(image_bytes)
    img_base64 = utils.encode_image_to_base64(annotated_image)
    return {"detections": result_json, "image": img_base64}
