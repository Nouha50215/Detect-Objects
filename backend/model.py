# Loads YOLO model + handles inference

from ultralytics import YOLO
import numpy as np
import cv2
from io import BytesIO
from PIL import Image
import json

model = YOLO("models/yolov8n.pt")

def predict(image_bytes):
    np_arr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    results = model(img)
    annotated = results[0].plot()
    result_json = json.loads(results[0].tojson())
    return result_json, annotated
