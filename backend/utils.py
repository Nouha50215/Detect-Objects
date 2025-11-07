# Optional helper functions (OpenCV, base64, etc.)

import base64
import cv2

def encode_image_to_base64(image):
    _, buffer = cv2.imencode(".jpg", image)
    return base64.b64encode(buffer).decode("utf-8")
